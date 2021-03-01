from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    isbn = db.Column(db.String(13), nullable=False)

    def __repr__(self):
        return f"<Book {self.id}>"


@app.route('/Res')
def result():
    books = Book.query.all()
    return render_template('result.html', books=books)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        t = request.form['title']
        a = request.form['author']
        i = request.form['isbn']
        book = Book(title=t, author=a, isbn=i)

        try:
            db.session.add(book)
            db.session.commit()
            return redirect('/')

        except:
            return "Error!"

    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
