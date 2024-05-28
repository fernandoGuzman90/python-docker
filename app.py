from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def sum_numbers():
    num1 = request.form['num1']
    num2 = request.form['num2']
    try:
        sum_result = float(num1) + float(num2)
        return render_template('index.html', result=sum_result, num1=num1, num2=num2)
    except ValueError:
        return render_template('index.html', error="Entrada no Válida, por favor Ingrese unicamente Números.", num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(debug=True)
