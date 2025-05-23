FROM quay.io/jupyter/scipy-notebook:2025-05-12
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
ENTRYPOINT ["chainlit", "run", "/home/jovyan/src/app.py", "--host", "0.0.0.0", "--watch"]
