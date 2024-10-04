FROM python:3.7-slim-buster
WORKDIR /nycopendata
COPY . /nycopendata

RUN apt update -y

RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
