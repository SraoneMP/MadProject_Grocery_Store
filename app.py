

from os import getenv
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# initially it was above import config but it showed error initialisation must be done after importing config
from dotenv import load_dotenv

# Load the .env file

app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = getenv(
    'SQLALCHEMY_TRACK_MODIFICATION')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

import models