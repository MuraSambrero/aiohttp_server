FROM python:3.11.9-slim-bookworm

RUN mkdir -p /angry_app
WORKDIR /angry_app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "entry.py"]