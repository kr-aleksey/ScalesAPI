import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from scales import Scales

logging.info('Started')

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
