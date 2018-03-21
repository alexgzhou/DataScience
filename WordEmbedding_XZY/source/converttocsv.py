# -*- coding: utf-8 -*-
# Export Oracle database tables to CSV files
# environment initialization
import cx_Oracle
import pandas as pd
import os  
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  

db = cx_Oracle.connect('read/read@10.12.43.223:1521/tjdb')
cursor = db.cursor()
sql = 'SELECT distinct ZHENDUANXX,ZHENDUANJY,ZHENDUANMS FROM tjgltest.by_tijianms '    
cursor.execute(sql)
result = cursor.fetchall()
df = pd.DataFrame(result)
df.to_csv("result1.csv")