FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["make", "-j3", "run-bot", "run-prod-server"]
