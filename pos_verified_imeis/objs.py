from datetime import datetime
from unicodedata import name
from pydantic import BaseModel

class verifyImeiObj(BaseModel):
    ver_uname: str
    ver_pwd: str
    imei: str
    def to_json(self):
        return {
            'ver_uname': self.ver_uname,
            'ver_pwd': self.ver_pwd,
            'imei': self.imei
        }

class VerUserInfoObj(BaseModel):
    uname: str
    pwd: str

addImei_ep = '/posImei/addImei'
checkImeiVerified_ep = '/posImei/checkImei'
changeVerUser_ep = '/posImei/changeVerUser'

ver_uname = '3451'
ver_pwd = '1306'
