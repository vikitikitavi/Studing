FROM python:3.6.1-alpine

EXPOSE 5000

COPY ./server.py  /source/server.py

RUN pip install flask

ENTRYPOINT ["python", "/source/server.py"]