from flask import Flask,render_template,request
import pymysql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/gets/',methods=['POST'])
def search():
    conn = pymysql.connect(user='root', host='127.0.0.1', passwd='123456', db='test',cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    S = request.values.get('question')
    sql = "select * from database1 where xingming like '%" + S + "%'"
    cur.execute(sql)
    datas = cur.fetchall()
    return render_template('search.html', items=datas)


app.run(debug=True)