from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.inference import predict_new
from utils.config import APP_NAME, VERSION, preprocessor,  xgboost_model, best_threshold
from utils.MachineData import MachineData

app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["*"],
   allow_headers=["*"],
)

@app.get('/', tags=['General'])
async def home():
    return {
        "mesage": f"Welcome to {APP_NAME} API v{VERSION}"
    }




@app.post("/predict/xgboost", tags=['Models']) 
async def predict_xgboost(data: MachineData) -> dict:
    try:
        print("Parsed input:", data.dict())
        result = predict_new(data=data, preprocessor=preprocessor, model=xgboost_model, best_threshold=best_threshold)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



