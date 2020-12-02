FROM python:3.7.9-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8

# Create exec:exec and dev -fixed python permissions
RUN sed -i '/999/d;' /etc/group
RUN addgroup -S -g 999 exec && adduser -u 999 -SDHG exec exec
RUN adduser -DH dev && adduser exec dev
RUN chown -R 999:999 /usr/local/bin/ /usr/local/lib/python3.7/
RUN chown -R exec:dev /app

USER exec:dev
