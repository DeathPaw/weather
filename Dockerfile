FROM python:3.8.10
RUN apt-get update -y && apt-get install -y python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "app.py", "--host=0.0.0.0"]