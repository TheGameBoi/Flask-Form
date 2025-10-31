from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]

    return render_template("index.html")



@app.route('/about')
def about():
    return render_template("about.html")



app.run(debug=True, port=5001)