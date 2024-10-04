import base64
import io
from wasabi import msg

# Import Unstructured library partition functions
try:
    from unstructured.partition.auto import partition
    from unstructured.partition.pdf import partition_pdf
    from unstructured.partition.image import partition_image
    from unstructured.partition.docx import partition_docx
    from unstructured.partition.doc import partition_doc
    from unstructured.partition.xlsx import partition_xlsx
    from unstructured.partition.csv import partition_csv
    from unstructured.partition.pptx import partition_pptx
    from unstructured.partition.ppt import partition_ppt
except ImportError:
    msg.warn("unstructured libraries not installed, OCR functionality will be limited.")

from goldenverba.components.document import Document, create_document
from goldenverba.components.interfaces import Reader
from goldenverba.server.types import FileConfig


class CustomUnstructuredReader(Reader):
    """
    The CustomUnstructuredReader reads text, images, PDFs, DOCX, and additional file types using the Unstructured library.
    """

    def __init__(self):
        super().__init__()
        self.name = "UnstructuredLibrary"
        self.description = "Ingests text, images, PDFs, DOCX, and other common file types using Unstructured"
        self.requires_library = ["unstructured"]
        self.extension = [
            "txt", ".py", ".js", ".html", ".css", ".md", ".mdx", ".json", ".pdf", ".docx", ".doc", ".pptx", ".ppt",
            ".xlsx", ".xls", ".csv", ".tsv", ".ts", ".tsx", ".vue", ".svelte", ".astro", ".php", ".rb", ".go", 
            ".rs", ".swift", ".kt", ".java", ".c", ".cpp", ".h", ".hpp", ".eml", ".msg", ".xml", ".epub", ".rtf", 
            ".odt", ".bmp", ".tiff", ".heic", ".jpg", ".jpeg", ".png"
        ]  # Supported file extensions

    async def load(self, config: dict, fileConfig: FileConfig) -> list[Document]:
        """
        Load and process a file based on its extension using the Unstructured library.
        """
        msg.info(f"Loading {fileConfig.filename} ({fileConfig.extension.lower()})")

        decoded_bytes = base64.b64decode(fileConfig.content)

        # Using Unstructured library to partition content
        try:
            if fileConfig.extension == "":
                file_content = fileConfig.content
            else:
                # Pass file-like object or file content to the partition function
                file_content = await self.partition_file(decoded_bytes, fileConfig.extension.lower())

            return [create_document(file_content, fileConfig)]
        except Exception as e:
            msg.fail(f"Failed to load {fileConfig.filename}: {str(e)}")
            raise

    async def partition_file(self, decoded_bytes: bytes, extension: str) -> str:
        """Partition the file using Unstructured's partition function, with hi_res or OCR strategy where appropriate."""
        file_bytes_io = io.BytesIO(decoded_bytes)

        # Specialized partitioning for PDFs, images, DOCX, DOC, XLSX, CSV, PPTX, and PPT
        if extension == "pdf":
            # For PDFs, apply the "hi_res" strategy for better layout and OCR
            elements = partition_pdf(file=file_bytes_io, strategy="hi_res", ocr_languages=["eng"])
        elif extension in ["bmp", "tiff", "heic", "jpg", "jpeg", "png"]:
            # For images, use the "ocr_only" strategy for text extraction
            elements = partition_image(file=file_bytes_io, strategy="ocr_only", languages=["eng"])
        elif extension == "docx":
            # Partition DOCX files
            elements = partition_docx(file=file_bytes_io)
        elif extension == "doc":
            # Partition DOC files
            elements = partition_doc(file=file_bytes_io)
        elif extension in ["xlsx", "xls"]:
            # Partition Excel files
            elements = partition_xlsx(file=file_bytes_io)
        elif extension == "csv":
            # Partition CSV files
            elements = partition_csv(file=file_bytes_io)
        elif extension == "pptx":
            # Partition PowerPoint (PPTX) files
            elements = partition_pptx(file=file_bytes_io)
        elif extension == "ppt":
            # Partition PowerPoint (PPT) files
            elements = partition_ppt(file=file_bytes_io)
        else:
            # Use the default partitioning function for other file types
            elements = partition(file=file_bytes_io)

        # Join extracted elements into text for further processing
        return "\n\n".join([str(el) for el in elements])

