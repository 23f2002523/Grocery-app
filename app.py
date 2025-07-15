from flask import Flask, render_template

app = Flask(__name__)
import config # config.py se configuration load karega
import routes  # routes.py se routes import karega
import models  # models.py se database models import karega
  
if __name__ == '__main__':
    app.run(debug=True)