FROM python:3.7.9-slim

RUN pip install Django graphine 

CMD sleep 3600
