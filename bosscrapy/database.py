#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
MYSQL_DB = 'bosscrawl'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_HOST = '127.0.0.1'


conn=MySQLdb.connect(host=MYSQL_HOST,
                   user=MYSQL_USER,
                   password=MYSQL_PASS,
                   db=MYSQL_DB,
                   charset='utf8mb4',
                   cursorclass=MySQLdb.cursors.DictCursor)

