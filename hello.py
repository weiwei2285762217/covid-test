from flask import Flask
app = Flask(__name__)

@app.route('/1')
def hello_world():
   return 'Hello World'
def hello_url():
   return 'hello url'
app.add_url_rule('/2', '2', hello_url)

if __name__ == '__main__':
   app.run(debug = True)