from http import client
from log_apis.objs import *
import json
import log_apis.tools as tooldb

class logs_api_action():
    def __init__(self, app, db) -> None:
        @app.post(addlogs_ep)
        def add_Log(item: logobj):
            db.put(json.dumps(item.to_json()))
            return {'status': 'ok'}

        @app.get(getlogs_ep)
        def get_logs():
            return db.fetch()
            return 'ok'

        @app.delete(dellogs_ep)
        def del_logs():
            res = db.fetch()
            for i in res._items:
                key = i['key']
                db.delete(key=key)
            return {'status': 'ok'}