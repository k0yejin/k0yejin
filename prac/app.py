from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') #타이틀기브라는걸로 뭔가를 받아와 변수에 넣어줌
   print(title_receive) #찍어주기
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청을 잘 받았어요!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)