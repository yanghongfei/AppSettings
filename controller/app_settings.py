#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 15:53
# @Author  : Fred Yang
# @File    : app_settings.py
# @Role    : settings Handler


import json
import tornado.web
from database import db_session
from models import AppSettings


class AppSettingsHandler(tornado.web.RequestHandler):
    """AppSettings配置路由"""

    def get(self, *args, **kwargs):
        """返回所有数据"""
        r_datas = []
        try:
            info = db_session.query(AppSettings).all()
            for data in info:
                info_data = {
                    'name': data.name,
                    'value': data.value
                }
                r_datas.append(info_data)
            resp = {
                'status': 0,
                'data': r_datas,
                'msg': '查询成功'
            }
            return self.write(resp)

        except Exception as e:
            print(e)
            db_session.rollback()

        # data = self.get_argument('name')
        # if isinstance(data,str):
        #     data = json.loads(data)
        #
        # print('222', data, type(data))
        # r_datas = []
        # for name in data:
        #     info = db_session.query(AppSettings).filter(AppSettings.name==name).first()
        #     info = {
        #         'name':name,
        #         'value':info.value
        #     }
        #     r_datas.append(info)
        # resp = {
        #         'status':0,
        #         'data':r_datas,
        #         'msg':'查询成功'
        #     }
        # self.write(resp)

    def post(self, *args, **kwargs):
        """新增配置信息"""
        data = json.loads(self.request.body.decode('utf-8'))
        name = data.get('name', None)
        value = data.get('value', None)

        try:
            name_info = db_session.query(AppSettings).filter(AppSettings.name == name).first()
            if name_info:
                return self.write(dict(status=-1, msg='Name already exist....'))

            else:
                db_session.add(AppSettings(name=name, value=value))
                db_session.commit()
                resp = {
                    'status': 0,
                    'msg': '添加成功'
                }
                return self.write(resp)

        except Exception as e:
            print(e)
            db_session.rollback()

    def put(self, *args, **kwargs):
        """更新配置"""
        data = json.loads(self.request.body.decode('utf-8'))
        name = data.get('name', None)
        value = data.get('value', None)

        try:
            update_info = {
                # "name": name,
                "value": value
            }
            db_session.query(AppSettings).filter(AppSettings.name == name).update(update_info)
            db_session.commit()
            resp = {
                'status': 0,
                'msg': '更新成功'
            }
            return self.write(resp)
        except Exception as e:
            print(e)
            db_session.rollback()

    def delete(self, *args, **kwargs):
        """删除配置信息"""
        data = json.loads(self.request.body.decode("utf-8"))
        name = data.get('name', None)
        try:
            db_session.query(AppSettings).filter(AppSettings.name == name).delete(synchronize_session=False)
            db_session.commit()
            resp = {
                'status': 0,
                'msg': '删除成功'
            }
            return self.write(resp)
        except Exception as e:
            print(e)
            db_session.rollback()
