#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 17:36
# @Author  : Fred Yang
# @File    : models.py
# @Role    : 数据库信息


from datetime import datetime
from database import Base
from sqlalchemy import Column
from sqlalchemy import String, Integer, DateTime, TIMESTAMP
from sqlalchemy.dialects.mysql import LONGTEXT
from database import init_db


class AppSettings(Base):
    __tablename__ = 'app_settings'
    id = Column(Integer, primary_key=True, autoincrement=True)  # ID 自增长
    name = Column(String(100), nullable=False)  # key
    value = Column(LONGTEXT, nullable=False)    # value
    create_at = Column(DateTime, nullable=False, default=datetime.now())  # 记录创建时间
    update_at = Column(TIMESTAMP, nullable=False, default=datetime.now())  # 记录更新时间



#init_db()  #第一次初始化使用