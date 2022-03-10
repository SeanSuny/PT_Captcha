# 基础镜像
FROM python:3.9-alpine

# 维护者信息
LABEL maintainer "SeanSuny"
LABEL org.opencontainers.image.source=https://github.com/SeanSuny/PT_Captcha


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && \
    apk add --no-cache jpeg-dev zlib-dev && \
    pip install -r /app/requirements.txt && \
    apk del .tmp && rm /app/requirements.txt

COPY ./captcha_app /app/captcha_app
COPY ./run.py /app/run.py

EXPOSE 5000
CMD ["python", "run.py"]

