#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import string,random
import openpyxl



def getModels(conn) :

    wb = openpyxl.Workbook()
    ws = wb.active

    #获取游标
    cursor=conn.cursor()
    cursor.execute("select id, code, name, en_name from tb_meta_model;")
    while 1:
        model=cursor.fetchone()
        if model is None:
            #表示已经取完结果集
            break
        print ('*'*40)    
        print ("model info: ", model)
        insertModelInfo(model, ws)

        getModelFields(conn, model, ws)
    cursor.close()

    wb.save('test.xlsx')

    return

def getModelFields(conn, model, ws) :
    model_id = model[0]
    cursor = conn.cursor()
    cursor.execute("select id, ' ', code, name, en_name, type, max_size, precition from tb_meta_modelfield where model_id=%s", (model_id))
    modelFields = cursor.fetchall()
    for modelField in modelFields:
        print(modelField)
        insertModelField(modelField, ws)
    cursor.close()
    return

def insertModelInfo(model, ws) :
    ws.append(model)
    return

def insertModelField(modelField, ws) :
    ws.append(modelField)
    return

def main() : 
    #打开数据库连接
    conn = pymysql.connect(host="localhost",user="metadata",password="123456",database="metadata_both",charset="utf8")
    # print (conn)
    # print (type(conn))

    getModels(conn)

    conn.commit()
    conn.close()
    return

if __name__ == '__main__':
    main()



