# -*- coding: utf-8 -*-
import json
import os

env = os.environ.get('APP_ENV','dev')
os.path.dirname(os.path.abspath(__file__)) + ""
# 加载对应环境的配置文件
with open(f'config/{env}.json', 'r') as f:
    config = json.load(f)