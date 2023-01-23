FROM python:3

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev

WORKDIR /app

ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY data ./data
COPY init_db.py .

CMD ["python", "./init_db.py"]
