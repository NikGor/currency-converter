from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from converter.currency_db import update_currency_rates
from converter.currency_logic import convert_currency_logic
from converter.db import create_database_if_not_exists, SessionLocal
from converter.models import Currency

app = FastAPI()
create_database_if_not_exists()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["OPTIONS", "POST", "GET"],
    allow_headers=["*"],
)


class ConversionRequest(BaseModel):
    amount: float
    currency_from: str
    currency_to: str


@app.post('/convert', summary="Currency conversion", tags=["Conversion"])
async def convert(conversion_request: ConversionRequest):
    try:
        result = convert_currency_logic(
            conversion_request.amount,
            conversion_request.currency_from,
            conversion_request.currency_to
        )
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post('/update-rates')
async def update_rates_endpoint():
    try:
        update_currency_rates()
        return {"message": "Currency rates updated successfully"}
    except Exception as e:
        # Здесь лучше использовать более конкретные исключения, если возможно
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/last-update')
async def last_update_endpoint():
    db = SessionLocal()
    try:
        last_update = (db.query(Currency).
                       order_by(Currency.
                       updated_at.desc()).
                       first())
        if last_update:
            return {"last_updated": last_update.updated_at}
        else:
            return {"last_updated": "No data available"}
    finally:
        db.close()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
