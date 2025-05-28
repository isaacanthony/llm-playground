FROM quay.io/jupyter/scipy-notebook:2025-05-12
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt && playwright install
ENTRYPOINT ["fastmcp", "run", "--host", "0.0.0.0", "--port", "9000", "--transport", "sse", "/home/jovyan/src/app.py"]
