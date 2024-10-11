FROM python:3.10-slim-buster
EXPOSE 8080
RUN pip install mlflow==2.16.2
ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080"]
