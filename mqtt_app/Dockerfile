FROM python:3.10

WORKDIR /python-docker
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-u", "app.py"]