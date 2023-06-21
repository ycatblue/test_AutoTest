# -*- coding: utf-8 -*-
# @Time     : 2023/6/21
# @Author   : ycat
# @File     : mysql_util.py
import pymysql

from utils.log_util import logger
from utils.read import base_data

data = base_data.read_ini()['mysql']
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB'],
}


class MysqlDb:
    def __init__(self):
        # mysql链接
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def select_db(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        return self.cur.fetchall()

    def execute_db(self, sql):
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.connect()
        except Exception as e:
            logger.info("执行sql出错了".format(e))


if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db("select code from users_verifycode where mobile = '13066807785' order by id desc limit 1")
    print(result)
