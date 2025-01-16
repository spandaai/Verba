FROM python:3.11
WORKDIR /Verba
COPY . /Verba
RUN pip install -e '.'
RUN pip install sentence-transformers transformers
EXPOSE 8000
CMD ["verba", "start","--port","8000","--host","0.0.0.0"]
