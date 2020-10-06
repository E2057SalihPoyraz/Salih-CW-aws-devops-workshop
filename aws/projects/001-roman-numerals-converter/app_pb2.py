from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_roman(num):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanvalue = ""
    for i,d in enumerate(sayi):
        while (num >= d):
            num -= d
            romanvalue += roman[i]
    return romanvalue

@app.route('/', methods=["GET"])
def main_get():
    return render_template('index.html', developer_name='E2057 Salih', not_valid=False)

@app.route('/', methods=["POST"])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='E2057 Salih', not_valid=True)

    number = int(alpha)
    if not 0 < number < 4000:
        return render_template('index.html', developer_name='E2057 Salih', not_valid=True)
    
    return render_template('result.html', developer_name='E2057 Salih',
    number_decimal=number, number_roman=convert_to_roman(number))

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)