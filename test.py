import pymysql

conn = pymysql.connect(host='localhost', user='root', 
                       password='123456',database='demo01',
                       port=3306,charset="utf8mb4")

def con_my_sql(sql_code):
    try:
        conn.ping(reconnect=True)  # 检测连接是否断开，如果断开则重新连接 保证数据库连接正常
        print(sql_code)
        #通过游标对象对数据库服务器发出sql语句
        cursor = conn.cursor(pymysql.cursors.DictCursor) #返回数据是字典类型 而不是数组
        cursor.execute(sql_code)
        # 提交
        conn.commit()
        #关闭连接
        conn.close()
        return cursor #普通执行返回1，就是执行正常
    
    except pymysql.MySQLError as err_massage:
        #回滚
        conn.rollback()
        #关闭连接
        conn.close()
        return type(err_massage),err_massage
    

#插入数据
# username= "张三"
# pwd = "123456"
# code = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')" % (username,pwd)
# print(con_my_sql(code))


# #查询数据
# username = "张三"
# code = "select * from login_user where username = '%s'" % (username)
# cursor_ans = con_my_sql(code)
# print(cursor_ans.fetchall()) #返回的是一个列表 里面是字典 查询测试






