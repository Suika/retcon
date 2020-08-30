FROM alpine:3.10
EXPOSE 80
WORKDIR /app
ENV UID=1000 GID=1000
ENTRYPOINT [ "sh", "/app/docker/entrypoint.sh"]
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:3000"]
VOLUME /app/db

COPY . /app
RUN apk add --update --no-cache  python3 su-exec
RUN pip3 install -r requirements.txt
