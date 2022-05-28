FROM python:3.8

ADD app.py .
ADD templates /templates
RUN pip3 install flask flask-restful psycopg2 requests
CMD ["python3","-m","flask","run","--host=0.0.0.0","--port=5000"]
