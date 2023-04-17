from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == 'root':
        result = math.sqrt(num1)
    elif operation == 'square':
        result = num1 ** 2
    elif operation == 'sin':
        result = math.sin(math.radians(num1))
    elif operation == 'cos':
        result = math.cos(math.radians(num1))
    else:
        return 'Invalid operation'

    return render_template('calculator.html', result=result, operation=operation)

if __name__ == '__main__':
    app.run()

