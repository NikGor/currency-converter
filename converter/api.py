from fastapi import FastAPI, HTTPException
from converter.currency import convert_currency_logic
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

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
    # Тут будет вызов функции обновления курсов валют
    return {"message": "Currency rates updated"}


@app.get('/last-update')
async def last_update_endpoint():
    # Тут будет запрос даты последнего обновления из БД
    return {"last_updated": "2023-01-01T00:00:00"}
