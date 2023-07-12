import logging

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from scales import Scales


scales = Scales()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/weight/{scales_id}", description='Get weight from scales')
async def get_weight(scales_id: int):
    try:
        weight = scales.get_weight(scales_id)
        status = scales.get_status(scales_id)
    except KeyError:
        raise HTTPException(404)
    return {'weight': weight, 'status': status}


@app.on_event("shutdown")
def shutdown_event():
    logging.info('Завершение работы')
    scales.shutdown()


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8001, log_level='info')
