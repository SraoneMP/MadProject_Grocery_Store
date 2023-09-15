from flask import  Flask, render_template, request, redirect, url_for, flash
from models import db, User, Product, Category, Cart
from app import app

@app.route('/')
def login():
    return render_template('login.html')