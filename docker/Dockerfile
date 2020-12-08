FROM python:3.7.9-alpine

ARG PORT=8000
ENV PORT=$PORT

ENV HOME=/app
ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8

# Fixed permissions, create exec:exec and dev:dev
RUN sed -i '/999/d;' /etc/group
RUN addgroup -S -g 999 exec && adduser -u 999 -SDHG exec exec
RUN adduser -DH dev && adduser exec dev
RUN chown -R 999:999 /usr/local/bin/ /usr/local/lib/python3.7/

ADD --chown=exec:dev . /app
WORKDIR /app

EXPOSE ${PORT}
VOLUME /app

USER exec:dev

ENTRYPOINT ["/app/scripts/startup.sh"]