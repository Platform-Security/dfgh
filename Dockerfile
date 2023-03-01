FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir requirements.txt
COPY . .
CMD ["python""app.py"]