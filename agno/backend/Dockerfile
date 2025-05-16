FROM python:3.13.3-alpine3.21
WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "/home/src/playground.py"]
