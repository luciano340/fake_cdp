FROM python:3.12.3-alpine3.18

RUN apk update \
    && apk --no-cache --update add build-base

RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    mariadb-connector-c-dev \
    libffi-dev \
    build-base

WORKDIR /app
COPY . .
RUN pip install -r requeriments.txt

EXPOSE 8000
ENTRYPOINT ["python", "-u" , "main.py"]
CMD []