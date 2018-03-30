# environment initialization
import cx_Oracle
db = cx_Oracle.connect('read/read@10.12.43.223:1521/tjdb')
cursor = db.cursor()
sql = 'SELECT distinct ZHENDUANXX,ZHENDUANJY,ZHENDUANMS FROM tjgltest.by_tijianms WHERE rownum <= 5' 
result = cursor.execute(sql)

#获取数据表的列名，并输出  
title = [i[0] for i in cursor.description]  
  
#格式化字符串  
g = lambda k:"%-8s" % k  
title =map(g,title)  
  
for i in title:  
    print (i),  
  
print(" ")
#输出查询结果  
for i in result.fetchmany(5):  
    for k in map(g,i):  
        print (k),  
    print (" ")
    
