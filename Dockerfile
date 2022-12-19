FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 2124

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "2124", "--reload"]