from flask import Flask

app=Flask(__name__)

#un decorador se usa con el 
@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'

app.run(debug=True)