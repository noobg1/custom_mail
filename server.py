import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import smtplib
from mail import mail
from email.mime.text import MIMEText

app = Flask(__name__)
appendtext = "Hello "

def sendMail(text,mailList):
    for recipitent in mailList:    	
    	mail(recipitent, text)

  
@app.route('/unsubscribe/<mailid>')
def unsubscribe(mailid):
	print mailid
	return "Unsubscribed!"

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def input():
    text = request.form['text']
    mailList = request.form['mailList']
    sendMail(text,mailList.split(","))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("2251"),
        debug=True 
    )
