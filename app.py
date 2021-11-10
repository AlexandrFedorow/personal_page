from flask import Flask, render_template
import config
app = Flask(__name__)


@app.route('/')
def main():
    config.ctr += 1
    return render_template('main.html', ctr=config.ctr)



if __name__ == "__main__":
   app.run()
