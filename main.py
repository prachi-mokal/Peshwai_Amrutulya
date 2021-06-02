from flask import Flask,render_template,redirect,request
from telegram.send_telegram_msg import send_notif_to_telegram
app = Flask(__name__)

telegram_id="1646790620:AAHpobzkyn5vI0bw_uKkRh7Zl8TH9Zm9wyo"
channel_id="-1001486695495"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message',methods=["post"])
def send_message():
    form_data = request.form

    name = form_data['name']
    email = form_data['email']
    mobile_number = form_data['mobile_number']
    message= form_data['message']
    telegram_message = "Name : "+name+"\nEmail : "+email+"\nMobile Number : "+mobile_number+"\nMessage : "+message

    send_notif_to_telegram(telegram_message,telegram_id,channel_id)

    print(name,email,mobile_number,message)
    return redirect("/")

app.run(debug=True)