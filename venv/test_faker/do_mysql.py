from pymysql import cursors,connect
'''
connect() 建立数据库的连接
cursor（）获取数据库的游标
execute（）执行sql语句
commit（）提交数据库的执行
close（）关闭数据库的连接
'''
class MySql:
    def do_mysql(self,sql):
        #连接数据库
        db = connect(host = 'localhost',user = 'root',password = '123456',
                          db ='test',charset ='utf8mb4',cursorclass =cursors.DictCursor)  #cursorclass查询结果采用字典输出
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        #sql 查询语句
        # sql = "select * from ceshi where cid = %s;"
        try:
            #执行SQL语句
            # cursor.execute(sql,(getsql))
            cursor.execute(sql)
            result = cursor.fetchall()  #使用 fetchone获取数据
            return result
        except:
            print("exectue  sql is wrong !")
        finally:
            db.close()  #关闭数据库连接


if __name__ == '__main__':
    sql_end = MySql().do_mysql("select max(cid)as cid from ceshi;")[0]['cid']
    print(sql_end)
    print(type(sql_end))