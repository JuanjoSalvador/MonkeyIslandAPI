FROM python:3.10.5-alpine3.16
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt

ADD src /app
