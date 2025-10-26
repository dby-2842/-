from flask import Flask,render_template,request ,redirect,url_for,session
from test import con_my_sql

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index_login():

    return render_template('login.html')

@app.route('/register')
def index_register():
    return render_template('register.html')

@app.route('/index')
def index():
    if "username" in session:
        current_user = session['username']   # 从session中获取用户名，传递给模板（变量名必须是user，与前端{% if user %}对应）
        return render_template('index.html',user=current_user)   # 关键：传递user变量
    else:
        return redirect(url_for("index_login"))

@app.route('/logout')
def index_logout():
    del session["username"]
    return redirect(url_for("index_login"))




@app.route('/login' ,methods=['POST','GET'])
def login():
    name = request.form.get('username')
    pwd = request.form.get('password')

    code = "select * from login_user where username = '%s'" % (name) 
    cursor_ans = con_my_sql(code)
    cursor_select =  cursor_ans.fetchall()    # 获取所有结果（列表）
    if len(cursor_select) > 0:  # 先判断列表是否有数据
        cursor_select = cursor_select[0]  # 有数据再取第0个元素
        if pwd == cursor_select['password']:
           session['username'] = name
           return redirect(url_for("index"))
        else:
            return "登录失败,密码错误!<a href='/'>返回登录页</a>"
    else:
        return "登录失败,用户名不存在！<a href='/register'>返回注册页</a>"





@app.route('/register' ,methods=['POST','GET'])
def register():
    name = request.form.get('username')
    pwd = request.form.get('password')
    code = "select * from login_user where username = '%s'" % (name) 
    cursor_ans = con_my_sql(code)
    cursor_select =  cursor_ans.fetchall()    # 获取所有结果（列表）
    if len(cursor_select) > 0:  # 判断列表是否有数据
        return "注册失败,用户名已存在! <a href='/'>返回登录页</a>"
    else:
        code = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')" % (name,pwd)
        con_my_sql(code)
        return "注册成功 <a href='/'>返回登录页</a>"







if __name__ == "__main__":
    app.run(debug=True,port=8080)



