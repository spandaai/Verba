FROM python:3.11

WORKDIR /Verba
COPY . /Verba

# Install project dependencies
RUN pip install -e '.'

# Install additional libraries
RUN pip install sentence-transformers transformers python-pptx olefile

EXPOSE 8000

CMD ["verba", "start", "--port", "8000", "--host", "0.0.0.0"]
