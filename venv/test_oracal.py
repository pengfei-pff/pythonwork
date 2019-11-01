# import cx_Oracle                                       #引用模块cx_Oracle
# conn=cx_Oracle.connect('klg/klg@10.111.32.24/orcl')    #连接数据库
# c=conn.cursor()                                        #获取cursor
# x=c.execute('select * from t_app_profile t')           #使用cursor进行各种操作
# print(x.fetchall())
# c.close()                                              #关闭cursor
# conn.close()                                           #关闭连接

import cx_Oracle
import time
import xlrd


def save_data():
    try:
        db = cx_Oracle.connect('klg/klg@10.111.32.24/orcl')
        cr = db.cursor()
    except:
        print('database connection faile')
    file_name = r'C:\Users\pengfei\Desktop\T_APP_PROFILE.xlsx'
    workbook = xlrd.open_workbook(file_name)
    booksheet = workbook.sheet_by_index(0)
    nrows = booksheet.nrows  # 行数
    ncols = booksheet.ncols  # 列数
    # print(ncols,nrows)
    for i in range(1,nrows):
        row_data = booksheet.row_values(i)
        print(row_data)
        # if row_data:
        #     sql_insert = 'insert into t_app_profile (APP_PROFILE_SEQ, APP_PROFILE_TIME, APP_PROFILE_APPROIND, APP_PROFILE_PRDTLINE, APP_PROFILE_PRODUCT, APP_PROFILE_BRANCH, APP_PROFILE_SPEC, APP_PROFILE_LOWRISK, APP_PROFILE_CHANNEL, APP_PROFILE_PAYMENT, APP_PROFILE_SMEINCOME, APP_PROFILE_LNINCOME, APP_PROFILE_SPINCOME, APP_PROFILE_CMNAME, APP_PROFILE_CMNO, PKEY, SYS_DATE)values (%s,%s,%s,%s,%s.%s,%s,%s,%s,%s,%s)'%(row_data[0], row_data[1], row_data[2],row_data[3], row_data[4], row_data[5], row_data[6], row_data[7], row_data[8], row_data[9], row_data[10], row_data[11], row_data[12], row_data[13], row_data[14],row_data[15], row_data[16],row_data[17])
        #     cr.execute(sql_insert)
        #     insert_line += 1
    # param = [('W2004', '19-08-2019', '6227002575040291457', 2, 10540, 34456, 45456, 54645, 4656456, 2, 645634, 75646, 445, 5464, 7536, '2', '1', '1', 1, '1')]
    # sql = "insert into t_app_card (PKEY, SYS_DATE, APP_PROFILE_SEQ, APP_CARD_RKFREQ1M, APP_CARD_RKAMT1M, APP_CARD_PERIAMT3M, APP_CARD_ACCUFREQ, APP_CARD_ACCUAMT, APP_CARD_HGAMT1M, APP_CARD_CONSUFREQ, APP_CARD_CONSUAMT, APP_CARD_LIMIT, APP_CARD_DRAWFREQ, APP_CARD_DRAWAMT, APP_CARD_BALANCE, APP_CARD_MINPYIND, APP_CARD_ADLIMIND, APP_CARD_INACTION, APP_CARD_MINPY3M, APP_CARD_ADLIMRSIND)values (:1)"
    # # cr.execute(sql)
    # cr.executemany(sql, param)
    # print('Table is ok')
    cr.close()
    db.commit()
    db.close()
if __name__ == '__main__':
    save_data()

