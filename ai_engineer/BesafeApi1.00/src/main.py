from fastapi import FastAPI
import pydantic
from src.statics import MODEL_VERSION,TextRequest,PredictionResponse, predict_threat

# INSTANTIATE API
app =FastAPI(title='Threat Classification Model')

@app.get('/')
def index():
    return{'message':'This is a text classiffication api'}

@app.post('/predict/', response_model=PredictionResponse)
def predict(request:TextRequest):
    label,prob =predict_threat(text=request.text)
    return{
        'prediction' : label,
        'confidence':prob,
        'model_version':MODEL_VERSION
    }
@app.get('/health')
def health():
    try:
        return {"status": "ok", "model_version": MODEL_VERSION}
    except Exception as e:
        return {"status": "error", "detail": str(e)}