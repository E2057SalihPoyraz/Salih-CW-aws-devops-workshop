from flask import Flask, render_template, request

import milliseconds

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        millisec = request.form["number"]
        converted = milliseconds.convert(millisec)
        if milliseconds.convert(millisec):
            return render_template("result.html", developer_name="E2057 Salih",
                milliseconds = millisec, result = converted)
        else:
            return render_template("index.html", developer_name="E2057 Salih", not_valid=True)

    else:
        return render_template("index.html", developer_name="E2057 Salih", not_valid=False)


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host = "0.0.0.0", port=80)