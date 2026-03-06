#  Text Classification API

### FastAPI + ONNX + Docker (Production Ready)

---

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="180"/>
</p>

<p align="center">
  <b>High-performance NLP inference service built for production deployment.</b>
</p>

---

## 📌 Overview

This repository contains a **Docker-ready, production-grade text classification API** built with:

* ⚡ **FastAPI** – High-performance ASGI framework
* 🚀 **ONNX Runtime** – Optimized model inference
* 🐳 **Docker** – Containerized deployment
* 🧠 External tokenizer handling
* 🔄 Model versioning support
* 🩺 Health check endpoint for cloud platforms
* 🏭 Gunicorn + UvicornWorker production server

The model was originally trained in TensorFlow/Keras and converted to ONNX for lightweight and scalable inference.

---

# 🏗 Architecture

```
Client
   ↓
Load Balancer / Cloud Platform
   ↓
Docker Container
   ↓
Gunicorn
   ↓
UvicornWorker
   ↓
FastAPI
   ↓
ONNX Runtime
   ↓
Prediction
```

---

# 📁 Project Structure

```
text-ml-api/
│
├── src/
│   ├── main.py                          # FastAPI entrypoint
│   ├── statics.py                       # Loads ONNX model + tokenizer
│   ├── train.py                         # Request/response validation
|   ├── test.py                          # Loads ONNX model + tokenizer
│   ├── data_explore.py                  # Request/response validation
│
├── models/
│       ├── BesafeV1_1.0.00.onnx
├── tokenizers/
│       └── BesafeV1_1.0.00.pkl
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# ✨ Features

* ✅ Accepts raw text input
* ✅ Converts text → tokenized sequence
* ✅ Runs ONNX inference
* ✅ Returns prediction + confidence
* ✅ Model version switching via environment variables
* ✅ Production-ready server setup
* ✅ Cloud deployment compatible
* ✅ Clean API documentation (Swagger UI)

---

# 🧪 API Endpoints

---

## 🏠 `GET /`

Basic API status.

**Response**

```json
{
  "message": "This is a text classiffication api"
}
```

---

## 🔍 `POST /predict`

Classifies input text.

### Request

```json
{
  "text": "Example sentence to classify"
}
```

### Response

```json
{
  "prediction": 1,
  "confidence": 0.8723,
  "model_version": "1.0.00"
}
```

---

## 🩺 `GET /health`

Used for container health monitoring.

### Response

```json
{
  "status": "ok",
  "model_version": "1.0.00"
}
```

If the model fails to load:

```json
{
  "status": "error",
  "detail": "error message"
}
```

---

# 🐳 Docker Setup (Production Ready)

---

## 1️⃣ Build Docker Image

```bash
docker build -t Besafe_ml-api .
```

---

## 2️⃣ Run Container

```bash
docker run -p 8000:8000 text-ml-api
```

Access API documentation:

```
http://localhost:8000/docs
```
---

# 🏭 Production Server

This project uses:

```
gunicorn -k uvicorn.workers.UvicornWorker
```

Why?

* Multi-worker support
* Process management
* Auto-restart on failure
* Production stability

Example internal command:

```bash
gunicorn src.main:app \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    -w 4
```

---

# 🔁 Model Versioning

Models are organized by version:

```
models/
├── v1/
├── v2/
├── v3/
```

# ☁️ Cloud Deployment Options

This container works on:

* Google Cloud Run
* Render
* Railway
* AWS ECS
* Azure Container Apps
* Any Docker-compatible infrastructure

Deployment steps:

1. Build Docker image
2. Push to container registry
3. Deploy container
4. Set `MODEL_VERSION`
5. Ensure `/health` is used as health check endpoint

---

# 🧠 Design Philosophy

This repository reflects real-world ML system design:

* Separation of model and preprocessing
* Lightweight inference runtime
* Scalable API structure
* Version-controlled models
* Containerized deployment

---

# 🧑‍💻 Development Mode

Run locally without Docker:

```bash
uvicorn src.main:app --reload
```

---

# 📝 License

MIT License

---

# ⭐ Final Note

Training a model is only half the job.

Shipping it reliably is engineering.

This repository demonstrates how to move from experimentation to production-ready ML deployment.

---