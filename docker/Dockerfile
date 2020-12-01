FROM python:3.7.9-alpine

# Create exec:exec  999:999 and fixed python permissions
RUN sed -i '/999/d;' /etc/group
RUN addgroup -S -g 999 exec && adduser -u 999 -SDHG exec exec
RUN chown -R 999:999 /usr/local/bin/ /usr/local/lib/python3.7/

ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8

WORKDIR /app

USER exec

CMD sleep 3600
