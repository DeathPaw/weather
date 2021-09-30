FROM python:latest
RUN apt-get update -y && apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "app.py"]