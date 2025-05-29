FROM quay.io/jupyter/scipy-notebook:2025-05-12
USER root
RUN apt-get update && apt-get upgrade -y
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt && playwright install --with-deps chromium
USER jovyan
ENTRYPOINT ["fastmcp", "run", "--host", "0.0.0.0", "--port", "9000", "--transport", "sse", "/home/jovyan/src/app.py"]
