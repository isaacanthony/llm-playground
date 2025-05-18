FROM python:3.13.3-alpine3.21
WORKDIR /home
RUN apk add apache-arrow-dev build-base cmake
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["chainlit", "run", "/home/src/app.py", "--host", "0.0.0.0", "--watch"]
