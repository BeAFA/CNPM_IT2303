from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = "nhungchubetliet=qsrdhuqwh123123ipsdjfg098suf8923u549ihg23wefdhgcyvuiadf6uqwyghryitu32e78y5gui235vgrtf"

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"]=4

cloudinary.config(cloud_name='ddc1ttqdu', api_key='516983137732254', api_secret='8NaIW_6b-VmQGPmy1AMVG6UkHGA')

db = SQLAlchemy(app)
login = LoginManager(app)