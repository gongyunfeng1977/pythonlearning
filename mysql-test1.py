#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import string,random


#打开数据库连接
conn = pymysql.connect(host="localhost",user="metadata",password="123456",database="pythonDB",charset="utf8")
# print (conn)
# print (type(conn))

#另一种打开数据库连接，不指定数据库
# conn=pymysql.connect(host="localhost",user="metadata",password="123456",database="pythonDB",charset="utf8")
# conn.select_db('pythondb')

#获取游标
cursor=conn.cursor()

#创建pythonDB数据库
# cursor.execute('CREATE DATABASE IF NOT EXISTS pythonDB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
# cursor.close()#先关闭游标
# conn.close()#再关闭数据库连接
# print('创建pythonDB数据库成功')

#创建user表
# cursor.execute('drop table if exists user')
# sql="""CREATE TABLE IF NOT EXISTS `user` (
# 	  `id` int(11) NOT NULL AUTO_INCREMENT,
# 	  `name` varchar(255) NOT NULL,
# 	  `age` int(11) NOT NULL,
# 	  PRIMARY KEY (`id`)
# 	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

# cursor.execute(sql)
# cursor.close()#先关闭游标
# conn.close()#再关闭数据库连接
# print('创建数据表成功')

# '''插入单条数据'''
# insert=cursor.execute("insert into user values(1,'tom',18)")
# print('添加语句受影响的行数：',insert)

# #另一种插入数据的方式，通过字符串传入值
# sql="insert into user values(%s,%s,%s)"
# cursor.execute(sql,(3,'kongsh',20))

# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')

#另一种插入数据的方式，通过字符串传入值
# sql="insert into user values(%s,%s,%s)"
# insert=cursor.executemany(sql,[(4,'wen',20),(5,'tom',10),(6,'test',30)])
# print ('批量插入返回受影响的行数：',insert)
# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')


# cursor.execute("select * from user;")
# while 1:
#     res=cursor.fetchone()
#     if res is None:
#         #表示已经取完结果集
#         break
#     print (res)
# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')


# cursor.execute("select * from user")
# #取3条数据
# resTuple=cursor.fetchmany(3)
# print(type(resTuple))
# for res in resTuple:
#     print(res)

# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')



# cursor.execute("select * from user")
# #取所有数据
# resTuple=cursor.fetchall()
# # print(type(resTuple))
# print ('共%d条数据'%len(resTuple))
# for res in resTuple:
#     print(res)

# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')




#更新一条数据
# update=cursor.execute("update user set age=100 where name='kongsh'")
# print ('修改后受影响的行数为：',update)
# #查询一条数据
# cursor.execute("select * from user where name='kongsh'")
# print(cursor.fetchone())
# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')




#更新前查询所有数据
# cursor.execute("select * from user where name in ('kongsh','wen');")
# print('更新前的数据为：')
# for res in cursor.fetchall():
#       print (res)

# print ('*'*40)      
# #更新2条数据
# sql="update user set age=%s where name=%s"
# update=cursor.executemany(sql,[(15,'kongsh'),(18,'wen')])

# #更新2条数据后查询所有数据
# cursor.execute("select * from user where name in ('kongsh','wen');")
# print('更新后的数据为：')
# for res in cursor.fetchall():
#       print (res)

# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')





# #删除前查询所有数据
# cursor.execute("select * from user;")
# print('删除前的数据为：')
# for res in cursor.fetchall():
#       print (res)

# print ('*'*40)      
# #删除1条数据
# cursor.execute("delete from user where id=1")

# #删除后查询所有数据
# cursor.execute("select * from user;")
# print('删除后的数据为：')
# for res in cursor.fetchall():
#       print (res)
# cursor.close()
# conn.commit()
# conn.close()
# print('sql执行成功')



# #获取游标
# cur=conn.cursor()
# #删除前查询所有数据
# cur.execute("select * from user;")
# print('删除前的数据为：')
# for res in cur.fetchall():
#       print (res)

# print ('*'*40)      
# #删除2条数据
# sql="delete from user where id=%s"
# cur.executemany(sql,[(3),(4)])

# #删除后查询所有数据
# cur.execute("select * from user;")
# print('删除后的数据为：')
# for res in cur.fetchall():
#       print (res)
# cur.close()
# conn.commit()
# conn.close()
# print('sql执行成功')


####################################################
#回滚事务示例
####################################################
#获取游标
# cur=conn.cursor()
# #修改前查询所有数据
# cur.execute("select * from user;")
# print('修改前的数据为：')
# for res in cur.fetchall():
#       print (res)

# print ('*'*40)      
# #更新表中第1条数据
# cur.execute("update user set name='xiaoxiaoxiaoxiaoren' where id=5")

# #修改后查询所有数据
# cur.execute("select * from user;")
# print('修改后的数据为：')
# for res in cur.fetchall():
#       print (res)
# print ('*'*40)
# #回滚事务
# conn.rollback()
# cur.execute("select * from user;")
# print('回滚事务后的数据为：')
# for res in cur.fetchall():
#       print (res)

# cur.close()
# conn.commit()
# conn.close()
# print('sql执行成功')
####################################################



####################################################
'''插入100条数据到数据库(每次插入一条)'''
####################################################
#获取游标
# cur=conn.cursor()

# #创建user表
# cur.execute('drop table if exists user')
# sql="""CREATE TABLE IF NOT EXISTS `user` (
# 	  `id` int(11) NOT NULL AUTO_INCREMENT,
# 	  `name` varchar(255) NOT NULL,
# 	  `age` int(11) NOT NULL,
# 	  PRIMARY KEY (`id`)
# 	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

# cur.execute(sql)

# #修改前查询所有数据
# cur.execute("select * from user;")
# print('修改前的数据为：')
# for res in cur.fetchall():
#       print (res)

# print ('*'*40)      
# #循环插入数据
# words=list(string.ascii_letters)
# print (words)
# sql="insert into user values(%s,%s,%s)"
# for i in range(100):
#       random.shuffle(words)#打乱顺序
#       cur.execute(sql,(i+1,"".join(words[:5]),random.randint(0,80)))

# #插入100条后查询所有数据
# cur.execute("select * from user;")
# print('修改后的数据为：')
# for res in cur.fetchall():
#       print (res)
# print ('*'*40)

# cur.close()
# conn.commit()
# conn.close()
# print('sql执行成功')

####################################################



####################################################
'''插入100条数据到数据库(一次插入多条)'''
####################################################
#获取游标
cur=conn.cursor()

#创建user表
cur.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) NOT NULL,
	  `age` int(11) NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cur.execute(sql)

#修改前查询所有数据
cur.execute("select * from user;")
print('修改前的数据为：')
for res in cur.fetchall():
      print (res)

print ('*'*40)      
#循环插入数据
words=list(string.ascii_letters)
sql="insert into user values(%s,%s,%s)"
random.shuffle(words)#打乱顺序
cur.executemany(sql,[(i+1,"".join(words[:5]),random.randint(0,80)) for i in range(100) ])

#插入100条后查询所有数据
cur.execute("select * from user;")
print('修改后的数据为：')
for res in cur.fetchall():
      print (res)
print ('*'*40)

cur.close()
conn.commit()
conn.close()
print('sql执行成功')

####################################################