

@app.route('/calculator/<int:num1>/<int:num2>/<operator>')
def calculator(num1,num2,operator):
    if operator == 'add':
        return  str(num1+num2)
    if operator == 'minus':
        return  str(num1-num2)
    if operator == 'divide':
        return  str(num1 / num2)
    if operator == 'multiply':
        return  str(num1 * num2)