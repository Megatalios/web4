from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    message = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Client %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about_us.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        name = request.form['name']
        mail = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']

        client = Client(name=name, mail=mail, phone_number=phone_number, message=message)
        try:
            db.session.add(client)
            db.session.commit()
            return redirect('/')

        except:
            return "При добавлении ваших данныхп произошла ошибка"
    else:
        return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)