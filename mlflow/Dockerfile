FROM python:3.13.3-alpine3.21
WORKDIR /home
RUN apk add apache-arrow-dev build-base cmake
RUN pip3 install mlflow==2.22.0
ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080"]
