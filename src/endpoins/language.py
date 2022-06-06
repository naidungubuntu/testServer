from fastapi import APIRouter
from fastapi import Query
from typing import Optional
import pandas as pd

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/language",
    tags=["get data multi language"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def language():
    df = pd.read_excel('././data/app_language.xlsx')
    df = df.fillna('')
    return {'status': 200, 'data': df.to_dict('record')}