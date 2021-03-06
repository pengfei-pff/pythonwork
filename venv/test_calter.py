import random,datetime
import pymysql
import time

class MyPyMysql:
    def __init__(self, host,username, password, db, charset='utf8'):
        self.host = host  # mysql主机地址
        # self.port = port  # mysql端口
        self.username = username  # mysql远程连接用户名
        self.password = password  # mysql远程连接密码
        self.db = db  # mysql使用的数据库名
        self.charset = charset  # mysql使用的字符编码,默认为utf8
        self.pymysql_connect()  # __init__初始化之后，执行的函数
    #随机生成身份证号
    def ident_generator(self):
        # 身份证号的前两位，省份代号
        sheng = (
            '11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
            '44',
            '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')

        # 随机选择距离今天在7000到25000的日期作为出生日期（没有特殊要求我就随便设置的，有特殊要求的此处可以完善下）
        birthdate = (datetime.date.today() - datetime.timedelta(days=random.randint(7000, 25000)))

        # 拼接出身份证号的前17位（第3-第6位为市和区的代码，中国太大此处就偷懒了写了定值，有要求的可以做个随机来完善下；第15-第17位为出生的顺序码，随机在100到199中选择）
        ident = sheng[random.randint(0, 31)] + '0101' + birthdate.strftime("%Y%m%d") + str(random.randint(100, 199))

        # 前17位每位需要乘上的系数，用字典表示，比如第一位需要乘上7，最后一位需要乘上2
        coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4,
               17: 2}
        summation = 0

        # for循环计算前17位每位乘上系数之后的和
        for i in range(17):
            summation = summation + int(ident[i:i + 1]) * coe[i + 1]  # ident[i:i+1]使用的是python的切片获得每位数字

        # 前17位每位乘上系数之后的和除以11得到的余数对照表，比如余数是0，那第18位就是1
        key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

        # 拼接得到完整的18位身份证号
        return ident + key[summation % 11]
    # 随机生成手机号码
    def createPhone(self):
        for k in range(10):
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                       "153", "155", "156", "157", "158", "159", "186", "187", "188", "189"]
            return str(random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8)))

    def pymysql_connect(self):
        # pymysql连接mysql数据库
        # 需要的参数host,port,user,password,db,charset
        self.conn = pymysql.connect(host=self.host,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset
                                    )
        # 连接mysql后执行的函数
        self.run(1,100)

    def run(self, nmin, nmax):
        #姓名组合列表
        fname = ['金', '赵', '李', '陈', '许', '龙', '王', '高', '张', '侯', '艾', '钱', '孙', '周', '郑']
        mname = ['玉', '明', '玲', '淑', '艳', '大', '小', '风', '雨', '雪', '天', '水', '奇', '鲸', '米', '晓', '泽', '恩', '葛','玄', '道','振', '隆', '奇']
        lname = ['玲', '芳', '明', '红', '国', '芬', '云', '娴', '隐','花', '叶', '黄', '亮', '锦', '茑', '军','印','凯']
        # 创建游标
        self.cur = self.conn.cursor()

        # 定义sql语句,插入数据
        sql = "INSERT INTO `test`.`ceshi` (`cid`, `name`, `idnumber`) VALUES (%s,%s,%s);"

        # 定义总插入行数为一个空列表
        data_list = []
        for i in range(nmin, nmax):
            #随机生成姓名
            pname = random.choice(fname) + random.choice(mname) + random.choice(lname)
            #随机生成手机号
            phone = self.createPhone()
            #随机生成的身份证号
            id = self.ident_generator()
            # 添加所有任务到总的任务列表
            result = (phone,pname,id)
            data_list.append(result)
            print(data_list)

        # 执行多行插入，executemany(sql语句,数据(需一个元组类型))
        content = self.cur.executemany(sql, data_list)
        if content:
            print('成功插入第{}条数据'.format(nmax - 1))

        # 提交数据,必须提交，不然数据不会保存
        self.conn.commit()


if __name__ == '__main__':
    start_time = time.time()  # 计算程序开始时间
    st = MyPyMysql('localhost', 'root', '123456', 'test')  # 实例化类，传入必要参数
    print('程序耗时{:.2f}'.format(time.time() - start_time))  # 计算程序总耗时




