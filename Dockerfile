FROM python:3.11

# Install system dependencies first
RUN apt-get update && apt-get install -y \
    libmagic1 \
    poppler-utils \
    tesseract-ocr \
    libreoffice \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

# Create and set permissions for unstructured temp directory
RUN mkdir -p /tmp/unstructured \
    && chmod 777 /tmp/unstructured

# Set working directory
WORKDIR /Verba

# Copy project files
COPY . /Verba

# Install the package in editable mode
RUN pip install -e '.'

# Expose the port
EXPOSE 8000

# Start the service
CMD ["verba", "start","--port","8000","--host","0.0.0.0"]
