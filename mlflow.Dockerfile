FROM python:3.7-slim-buster
EXPOSE 8080
RUN pip install mlflow
ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080"]
