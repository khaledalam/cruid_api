FROM tiangolo/uvicorn-gunicorn:python3.10-slim

LABEL maintainer="Khaled Alam <khaledalam.net@gmail.com>"

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

EXPOSE 8888

CMD uvicorn main:fastAPI --host 0.0.0.0 --port 8888 --reload