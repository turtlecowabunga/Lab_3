from math import sqrt
from flask import Flask, render_template, request
def func(a, b, c):
    if (a == 0): return "Данное уравнение не квадратное."
    D = b**2 - 4 * a * c
    if (D < 0):
        real_part = round(-b/(2*a),3)
        imaginary_part= round(sqrt(abs(D))/(2 * abs(a)), 3)
        if real_part % 1 == 0: real_part = int(real_part)
        if imaginary_part % 1 == 0: imaginary_part= int(imaginary_part)

        x1 = f"{real_part}+{imaginary_part}i"
        x2 = f"{real_part}-{imaginary_part}i"
    else:
        x1 = round((-b+sqrt(D))/(2*a),3)
        x2 = round((-b-sqrt(D))/(2*a),3)

        if x1 % 1 == 0: x1 = int(x1)
        if x2 % 1 == 0: x2 = int(x2)
    return x1, x2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def solve():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    result = func(a, b, c)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()