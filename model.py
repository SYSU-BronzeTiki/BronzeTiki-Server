#encoding: utf-8

import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__, static_folder='./dist/static', template_folder='./dist')
app.config.from_object(config)
db = SQLAlchemy(app)

app.secret_key = b'\x98\xc0&\xa1\x15\xaf\x8b\x16\x99\xcb\x90\x17$\xf1\xec\xfd\xe1\xadNo\xa3g\xae\xf6'

salt = "2sjx*7sa8*(0&^@9de2-fd23+fd*/ds"

# Data table User
# create table user (
#     username varchar(50),
#     password varchar(8),
#     avator BLOB,
#     nickname varchar(50),
#     paypassword varchar(8),
#     description varchar(256),
#     money int,
#     # commentID int,
#     primary key (username)
# )
class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(256), nullable=False)
    avator = db.Column(db.BLOB)
    nickname = db.Column(db.String(50))
    paypassword = db.Column(db.String(8))
    description = db.Column(db.String(256))
    money = db.Column(db.Integer)
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

# Data table Movie
# create table movie (
#     movieID int,
#     movieName varchar(50),
#     poster BLOB,
#     primaryActors varchar(256),
#     duration datetime,
#     movieType varchar(50),
#     description varchar(256),
#     rating int
#     primary key (movieID)
# )
class Movie(db.Model):
    __tablename__ = 'movie'
    movieID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movieName = db.Column(db.String(50), nullable=False)
    poster = db.Column(db.BLOB)
    primaryActors = db.Column(db.String(256))
    duration = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    movieType = db.Column(db.String(50))
    description = db.Column(db.String(256))
    rating = db.Column(db.Integer)
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

# Data table Comment
# create table comment (
#     commentID int,
#     time datetime,
#     rating int,
#     description varchar(256),
#     username varchar(50),
#     movieID int,
#     primary key (commentID),
#     foreign key (username) references user(username),
#     foreign key (movieID) references movie(movieID)
# )
class Comment(db.Model):
    __tablename__ = 'comment'
    commentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    rating = db.Column(db.Integer)
    description = db.Column(db.String(256)),
    username = db.Column(db.String(50), db.ForeignKey('user.username'))
    movieID = db.Column(db.Integer, db.ForeignKey('movie.movieID'))
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

# Data table MovieHall
# create table movieHall(
#     movieHallID int,
#     primary key (movieHallID)
# )
class MovieHall(db.Model):
    __tablename__ = 'movieHall'
    movieHallID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(256))
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

# Data table Screen
# create table screen (
#     screenID int,
#     beginTime datetime,
#     ticketPrice int,
#     movieHallID int,
#     movieID int,
#     primary key (screenID),
#     foreign key (movieHallID) references movieHall(movieHalllID),
#     foreign key (movieID) references movie(movieID)
# )
class Screen(db.Model):
    __tablename__ = 'screen'
    screenID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    beginTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ticketPrice = db.Column(db.Integer)
    movieHallID = db.Column(db.Integer)
    movieID = db.Column(db.Integer)
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

# Data table Seat
# create table seat (
#     seatID int,
#     isAvailable boolean,
#     screenID int,
#     primary key (seatID),
#     foreign key (screenID) references screen(screenID)
# )
class Seat(db.Model):
    __tablename__ = 'seat'
    seatID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isAvailable = db.Column(db.Boolean, nullable=False)
    screenID = db.Column(db.Integer, db.ForeignKey('screen.screenID'))
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

# Data table MovieOrder 
# create table movieorder (
#     orderID int,
#     genTime datetime,
#     payTime datetime,
#     price int,
#     username varchar(50),
#     # movieHallID int,
#     # movieID int,
#     seatID int,
#     primary key (orderID),
#     foreign key (username) references user(username),
#     # foreign key (movieHallID) references movieHall(movieHallID),
#     # foreign key (movieID) references movie(movieID),
#     foreign key (seatID) references seat(seatID)
# )
class Order(db.Model):
    __tablename__ = 'movieorder'
    orderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    payTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    price = db.Column(db.Integer)
    username = db.Column(db.String(50), db.ForeignKey('user.username'))
    seatID = db.Column(db.Integer, db.ForeignKey('seat.seatID'))
    __table_args__ = {
        "mysql_charset" : "utf8"
    }

