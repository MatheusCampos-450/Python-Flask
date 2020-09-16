from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Hello world!"


# Recebendo uma string como Route params
@app.route("/test", defaults={'name': None}) # Definindo valor padrão como None
@app.route("/test/<name>") # Passando route params
def test(name):
    if name:
        print(type(name))
        return "Olá, %s!" % name
    else:
        return "olá, usuário!" 
    
    
# Recebendo um integer como route params
@app.route("/numero/<int:id>")
def numero(id):
    print(type(id))
    return ""


# Limitando métodos que podem ser usados na página
@app.route("/method/", methods=['GET'])
def method():
    return "Oi!"