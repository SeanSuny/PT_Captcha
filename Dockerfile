FROM alpine:latest

WORKDIR /app

COPY *.txt *.py /app
COPY captcha_app /app/captcha_app

RUN set -eux \
&& apk add --update --no-cache --virtual .build-deps gcc libc-dev linux-headers python3-dev py3-pip \
&& apk add --no-cache tzdata jpeg-dev zlib-dev python3 \
&& pip install -r /app/requirements.txt --no-cache-dir \
&& rm -rf /var/cache/apk/* \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& apk del --no-network .build-deps \
&& rm -rf /app/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "run.py"]

