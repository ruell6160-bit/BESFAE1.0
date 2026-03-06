
FROM python:3.10-slim

WORKDIR /src

COPY ai_engineer/BesafeApi1.00/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ai_engineer/BesafeApi1.00 ./BesafApi1.00

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "BesafeApi1.00.src.main:app", "--bind", "0.0.0.0:8000"]
