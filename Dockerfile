FROM python:3.7-slim-buster
WORKDIR frontend
COPY requirements.txt .
COPY frontend .

RUN apt update -y

RUN pip install flask pandas mlflow
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
