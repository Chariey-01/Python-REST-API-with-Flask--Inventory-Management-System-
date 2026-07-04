from flask import Flask
from routes import register_endponts

app = Flask(__name__)

register_endponts(app)

if __name__=="__main__":
  app.run(debug=True)