from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# ✅ Mail Config (make sure you enable "App Passwords" in Gmail security settings)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='harsh07tadokar@gmail.com',
    MAIL_PASSWORD='cdau wlmg yugu cosf'   # ❌ Use App Password, not your Gmail login password
)

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def port():
    success = False  # default
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')

            mail.send_message(
                'New message from ' + name,
                sender=email,
                recipients=['harsh07tadokar@gmail.com'],
                body=message
            )
            success = True  # ✅ only after successful send
        except Exception as e:
            print("Error sending email:", e)
            success = False

    return render_template('index.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)
