from datetime import datetime
import pos_verified_imeis.objs as Objs
import json

class posImei_api_action():
    def __init__(self, app, db) -> None:

        @app.post(Objs.addImei_ep)
        def dang_ky_imei_moi(info: Objs.verifyImeiObj):
            if info.ver_uname == Objs.ver_uname and info.ver_pwd == Objs.ver_pwd:
                newObj = json.dumps(info.to_json())
                db.put(newObj)
                return {'status': True, 'msg': 'Bạn đã xác nhận thiết bị thành công'}
            else:
                return {'status': False, 'msg': 'Vui lòng nhập đúng thông tin thể hiện bạn có quyền xác nhận thiết bị'}

        @app.get(Objs.checkImeiVerified_ep)
        def kiem_tra_imei_hop_le(imei: str):
            res = db.fetch()
            if res._count>0:
                for item in res._items:
                    js = json.loads(item['value'])
                    if js['imei'] ==  imei:
                        return {'status': True, 'msg': 'valid imei'}
                return {'status': False, 'msg': 'Thiết bị này chưa có mã xác nhận'}
            else:
                return {'status': False, 'msg': 'Thiết bị này chưa có mã xác nhận'}

        @app.post(Objs.changeVerUser_ep)
        def thay_doi_thong_tin_nguoi_verify(info: Objs.VerUserInfoObj):
            Objs.ver_uname = info.uname
            Objs.ver_pwd = info.pwd
            return {'status': True}

        @app.get('/posImei/fetchAll')
        def lay_danh_sach_imeis():
            return db.fetch()
        
        @app.get('/posImei/deleteAll')
        def xoa_tat_ca_imeis(pwd: str):
            if pwd != '123':
                return {'status': False}
            res = db.fetch()
            for i in res._items:
                key = i['key']
                db.delete(key=key)
            return {'status': True}

        @app.get('/posImei/deleteOne')
        def xoa_mot_imei_nao_do(imei: str, pwd: str):
            if pwd != '123':
                return {'status': False}
            res = db.fetch()
            for i in res._items:
                if i['value']==imei:
                    key = i['key']
                    db.delete(key=key)
                    return {'status': True}
            return {'status': False, 'msg':'Invalid Imei'}