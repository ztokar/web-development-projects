from flask import Flask, render_template
from datetime import date
#datetime.dateime.now().year
# calling the today
# function of date class


app=Flask(__name__)

@app.route('/')
def simple_app():
    today = date.today()
    return render_template("index.html",now=today)

if __name__ == "__main__":
    app.run(debug=True)
