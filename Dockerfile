FROM python:3.8

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY src src

ENV FLASK_ENV=development
ENV FLASK_APP=app

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
