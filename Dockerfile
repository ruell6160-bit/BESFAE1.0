# Base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI app into container
COPY ai_engineer/BesafeApi1.00 ./BesafeApi1.00

# Expose the port Railway uses
EXPOSE 8000

# Run FastAPI via Gunicorn + Uvicorn worker
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "BesafeApi1.00.src.main:app", "--bind", "0.0.0.0:8000"]