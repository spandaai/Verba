import base64
import io
import subprocess
from typing import List, Optional
from wasabi import msg
from goldenverba.components.document import Document, create_document
from goldenverba.components.interfaces import Reader
from goldenverba.server.types import FileConfig

# Primary unstructured imports with error handling
try:
    from unstructured.partition.auto import partition
    from unstructured.partition.pdf import partition_pdf
    from unstructured.partition.docx import partition_docx
    from unstructured.partition.doc import partition_doc
    from unstructured.partition.pptx import partition_pptx
    from unstructured.partition.ppt import partition_ppt
    from unstructured.partition.xlsx import partition_xlsx
    from unstructured.partition.csv import partition_csv
    from unstructured.partition.text import partition_text
    UNSTRUCTURED_AVAILABLE = True
except ImportError:
    msg.warn("unstructured library not installed, falling back to alternative methods")
    UNSTRUCTURED_AVAILABLE = False

# Fallback imports - only import if needed
PyPDF2 = None
pdfplumber = None
docx = None
Presentation = None

class CustomUnstructuredReader(Reader):
    """
    A reader that uses the Unstructured library primarily, with fallbacks only when necessary.
    Implements the Reader interface from goldenverba.components.interfaces.
    """

    def __init__(self):
        super().__init__()
        self.name = "UnstructuredLibrary"
        self.description = "Ingests documents using Unstructured library with smart fallbacks"
        self.requires_library = ["unstructured"]
        self.extension = [
            "pdf", "xlsx", "csv", "docx", "doc", "pptx", "ppt", "txt"
        ]
        self._check_dependencies()

    def _check_dependencies(self) -> None:
        """Check system dependencies for unstructured partitioning."""
        self.has_poppler = False
        self.has_libreoffice = False
        
        try:
            subprocess.run(['pdfinfo', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.has_poppler = True
        except FileNotFoundError:
            msg.warn("Poppler not found - PDF processing may be limited")

        try:
            subprocess.run(['soffice', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.has_libreoffice = True
        except FileNotFoundError:
            msg.warn("LibreOffice not found - DOC/PPT processing may be limited")

    def _load_fallback_libraries(self, file_type: str) -> None:
        """Lazily load fallback libraries only when needed."""
        global PyPDF2, pdfplumber, docx, Presentation

        if file_type == "pdf" and not (PyPDF2 and pdfplumber):
            try:
                import PyPDF2
            except ImportError:
                msg.warn("PyPDF2 not installed")
            try:
                import pdfplumber
            except ImportError:
                msg.warn("pdfplumber not installed")

        elif file_type in ["doc", "docx"] and not docx:
            try:
                import docx
            except ImportError:
                msg.warn("python-docx not installed")

        elif file_type in ["ppt", "pptx"] and not Presentation:
            try:
                from pptx import Presentation
            except ImportError:
                msg.warn("python-pptx not installed")

    async def _process_pdf(self, file_bytes: bytes) -> str:
        """Process PDF with unstructured first, then fallbacks if needed."""
        try:
            if self.has_poppler:
                file_obj = io.BytesIO(file_bytes)
                elements = partition_pdf(file=file_obj, strategy="fast")
                text = "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
                if text.strip():
                    return text
                msg.warn("Unstructured PDF processing produced no text, trying fallbacks")
        except Exception as e:
            msg.warn(f"Unstructured PDF processing failed: {str(e)}")

        # Load fallback libraries only if needed
        self._load_fallback_libraries("pdf")
        
        # Try PyPDF2
        if PyPDF2:
            try:
                with io.BytesIO(file_bytes) as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    text = "\n\n".join(page.extract_text() for page in reader.pages)
                    if text.strip():
                        return text
            except Exception as e:
                msg.warn(f"PyPDF2 extraction failed: {str(e)}")

        # Try pdfplumber as last resort
        if pdfplumber:
            try:
                with io.BytesIO(file_bytes) as pdf_file:
                    with pdfplumber.open(pdf_file) as pdf:
                        text = "\n\n".join(page.extract_text() for page in pdf.pages)
                        if text.strip():
                            return text
            except Exception as e:
                msg.warn(f"pdfplumber extraction failed: {str(e)}")

        msg.warn("All PDF extraction methods failed")
        return ""

    async def _process_docx(self, file_bytes: bytes) -> str:
        """Process DOCX with unstructured first, then fallback if needed."""
        try:
            file_obj = io.BytesIO(file_bytes)
            elements = partition_docx(file=file_obj)
            text = "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
            if text.strip():
                return text
            msg.warn("Unstructured DOCX processing produced no text, trying fallback")
        except Exception as e:
            msg.warn(f"Unstructured DOCX processing failed: {str(e)}")

        # Load fallback library only if needed
        self._load_fallback_libraries("docx")
        
        if docx:
            try:
                doc = docx.Document(io.BytesIO(file_bytes))
                return "\n".join(paragraph.text for paragraph in doc.paragraphs)
            except Exception as e:
                msg.warn(f"DOCX fallback extraction failed: {str(e)}")
        
        return ""

    async def _process_doc(self, file_bytes: bytes) -> str:
        """Process DOC with unstructured first, then fallback if needed."""
        try:
            if self.has_libreoffice:
                file_obj = io.BytesIO(file_bytes)
                elements = partition_doc(file=file_obj)
                text = "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
                if text.strip():
                    return text
                msg.warn("Unstructured DOC processing produced no text, trying fallback")
        except Exception as e:
            msg.warn(f"Unstructured DOC processing failed: {str(e)}")

        # Try basic text extraction
        try:
            text = file_bytes.decode('utf-8', errors='ignore')
            if text.strip():
                return text
        except Exception as e:
            msg.warn(f"Basic text extraction failed: {str(e)}")
        
        return ""

    async def _process_pptx(self, file_bytes: bytes) -> str:
        """Process PPTX with unstructured first, then fallback if needed."""
        try:
            file_obj = io.BytesIO(file_bytes)
            elements = partition_pptx(file=file_obj)
            text = "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
            if text.strip():
                return text
            msg.warn("Unstructured PPTX processing produced no text, trying fallback")
        except Exception as e:
            msg.warn(f"Unstructured PPTX processing failed: {str(e)}")

        # Load fallback library only if needed
        self._load_fallback_libraries("pptx")
        
        if Presentation:
            try:
                prs = Presentation(io.BytesIO(file_bytes))
                text_runs = []
                for slide in prs.slides:
                    for shape in slide.shapes:
                        if hasattr(shape, "text"):
                            text_runs.append(shape.text)
                return "\n\n".join(text_runs)
            except Exception as e:
                msg.warn(f"PPTX fallback extraction failed: {str(e)}")
        
        return ""

    async def _process_ppt(self, file_bytes: bytes) -> str:
        """Process PPT with unstructured first, then fallback if needed."""
        try:
            if self.has_libreoffice:
                file_obj = io.BytesIO(file_bytes)
                elements = partition_ppt(file=file_obj)
                text = "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
                if text.strip():
                    return text
                msg.warn("Unstructured PPT processing produced no text, trying fallback")
        except Exception as e:
            msg.warn(f"Unstructured PPT processing failed: {str(e)}")

        # Try basic text extraction
        try:
            text = file_bytes.decode('utf-8', errors='ignore')
            if text.strip():
                return text
        except Exception as e:
            msg.warn(f"Basic text extraction failed: {str(e)}")
        
        return ""

    async def _process_xlsx(self, file_bytes: bytes) -> str:
        """Process XLSX with unstructured."""
        try:
            file_obj = io.BytesIO(file_bytes)
            elements = partition_xlsx(file=file_obj)
            return "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
        except Exception as e:
            msg.warn(f"XLSX processing failed: {str(e)}")
            return ""

    async def _process_csv(self, file_bytes: bytes) -> str:
        """Process CSV with unstructured."""
        try:
            file_obj = io.BytesIO(file_bytes)
            elements = partition_csv(file=file_obj)
            return "\n\n".join([str(el) for el in elements if hasattr(el, 'text')])
        except Exception as e:
            msg.warn(f"CSV processing failed: {str(e)}")
            return ""

    async def load(self, config: dict, fileConfig: FileConfig) -> List[Document]:
        """Load and process a file, returning a list of Document objects."""
        try:
            msg.info(f"Processing {fileConfig.filename}")
            decoded_bytes = base64.b64decode(fileConfig.content)
            extension = fileConfig.extension.lower()

            # Process based on file extension
            content = ""
            if extension == "pdf":
                content = await self._process_pdf(decoded_bytes)
            elif extension == "docx":
                content = await self._process_docx(decoded_bytes)
            elif extension == "doc":
                content = await self._process_doc(decoded_bytes)
            elif extension == "pptx":
                content = await self._process_pptx(decoded_bytes)
            elif extension == "ppt":
                content = await self._process_ppt(decoded_bytes)
            elif extension == "xlsx":
                content = await self._process_xlsx(decoded_bytes)
            elif extension == "csv":
                content = await self._process_csv(decoded_bytes)
            elif extension == "txt":
                content = decoded_bytes.decode('utf-8', errors='ignore')
            else:
                msg.warn(f"Unsupported extension: {extension}")
                content = ""

            return [create_document(content, fileConfig)]

        except Exception as e:
            msg.fail(f"Failed to process {fileConfig.filename}: {str(e)}")
            raise

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"

    def __repr__(self) -> str:
        return f"CustomUnstructuredReader(extensions={self.extension})"