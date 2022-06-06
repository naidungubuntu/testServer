from fastapi import APIRouter
from fastapi import Query
from typing import Optional
import pandas as pd
import json

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/menu",
    tags=["get menu products", 'get combos', 'get extras', 'get spices'],
    responses={404: {"description": "Not found"}}
)

@router.get('/emenus')
async def get(channel=1):
    with open('././data/menu.txt', mode='r', encoding='utf8') as f:
        data = f.readlines()[0]
        return {'status': 200, 'data': json.loads(data)}

@router.get('/combos')
async def get():
    with open('././data/combo.txt', mode='r', encoding='utf8') as f:
        data = f.readline()
        return {'status': 200, 'data': json.loads(data)}

@router.get('/extras')
async def get():
    with open('././data/extra.txt', mode='r', encoding='utf8') as f:
        data = f.readline()
        return {'status': 200, 'data': json.loads(data)}

@router.get('/spices')
async def get():
    with open('././data/spices.txt', mode='r', encoding='utf8') as f:
        data = f.readline()
        return {'status': 200, 'data': json.loads(data)}

@router.get('/keys')
async def get():
    source = '''
    {"Success":true,"Data":{"sizeS":{"vi":"S","en":"S"},"sizeM":{"vi":"M","en":"M"},"sizeL":{"vi":"L","en":"L"},"spiceNo":{"vi":"Không","en":"No"},"spiceLess":{"vi":"Ít","en":"Less"},"spiceMedium":{"vi":"Vừa","en":"Medium"},"spiceMuch":{"vi":"Nhiều","en":"More"}}}
    '''
    js = json.loads(source)
    return {'status': 200, 'data': js}
