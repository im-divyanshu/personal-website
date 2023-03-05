#using python version 3.10.6
from flask import Flask,render_template,request
import smtplib
# importing a local file which has mail and password
import mail_adress


app=Flask(__name__)

def send_mail(name,email,subject,massage):
    # using those local files to login
    mailadress=mail_adress.mails["sender"]
    password1=mail_adress.mails["sender_password"]
    reciver=mail_adress.mails["reciever"]
    massage_=f"subject:{subject}\n\n{name} says \n{massage}\nhis email is {email}"
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=mailadress,password=password1)
    connection.sendmail(from_addr=mailadress,to_addrs=reciver,msg=massage_)
    connection.close()

@app.route('/')
def index():
    print("route accessed")
    return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/banner')
def banner():
    return render_template("banner.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/send_mail')
def mailsent():
    name=request.args.get('Name')
    emai=request.args.get('E-mail')
    subject=request.args.get('Subject')
    massage=request.args.get('Massage')
    try:
        send_mail(name,emai,subject,massage)
    except:
        return render_template("failedtomail.html")
    return render_template("mailsent.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)