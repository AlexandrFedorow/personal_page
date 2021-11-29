from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Count(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    n = db.Column(db.Integer(), primary_key=False)

    def __repr__(self):
        return '<Count %r' % self.id


@app.route('/')
def main():
    line = Count.query.filter_by(id=1).all()
    line[0].n += 1
    db.session.commit()
    nline = Count.query.filter_by(id=1).all()
    return render_template('main.html', ctr=nline[0].n)


if __name__ == "__main__":
   app.run()
