from datetime import datetime
from unicodedata import name
from pydantic import BaseModel

class logobj(BaseModel):
    name: str = None
    shopid: int = 0
    detail: str = None
    logTime: datetime
    uid: int = 0

    def to_json(self):
        return {
            'name': self.name,
            'shopid': self.shopid,
            'detail': self.detail,
            'logTime': str(self.logTime),
            'uid': self.uid
        }

addlogs_ep = '/logs-api/addLog'
getlogs_ep = '/logs-api/getLogs'
dellogs_ep = '/logs-api/deleteLogs'