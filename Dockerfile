FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
