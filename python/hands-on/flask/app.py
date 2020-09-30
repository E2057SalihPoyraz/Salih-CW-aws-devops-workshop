from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", salih = True)

@app.route("/for")
def for_example():
    names = ["Feyzullah", "Salih", "Gokhan", "Murat", "Veysel", "Serdar"]
    return render_template("deneme.html", isimler = names)





if __name__ == "__main__":
    app.run(debug = True)