
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home")
def home():
    # jinja 2
    return render_template("home.html", app_name="WIX")

@app.route("/author")
def author():
    return render_template("author.html", author_name="Francisco", author_age="33", author_bio="Mi biografia")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/saludar")
def saludo():
    #http://localhost:50000/saludar?name=Sebastian
    name = request.args.get("name")
    if not name:
        return "No hay nadie"
    return "Hola " + name

@app.route("/echo")
def echo():
    response_string = "Recibi: "
    params = request.args
    for k, v in params.iteritems():
        response_string = response_string + ("%s ------ %s, " % (k,v))
    return response_string

@app.route("/list")
def lista():
    lista = [
        {"nombre": "Ximena", "apodo": "Jimmy"},
        {"nombre": "Antonio", "apodo": "Tonny"},
        {"nombre": "Julian", "apodo": "Jules"},
    ]
    return render_template("list.html", lista=lista)

@app.route("/alumno/<ids>")
def get_by_apodo(ids):
    alumnos = {
                'ximena': {"nombre": "Ximena Ortega", "edad": "23", "bio": "Alumna DevF" },
                'tono': {"nombre": "Antonio Banderas", "edad": "26", "bio": "Le dicen el Patronceto"},
                'pablo': {"nombre": "Pablo Velazquez", "edad": "25", "bio": "Colorear"}
    }

    alumno = alumnos.get(ids)

    return render_template("alumno.html", alumno=alumno)


if __name__ == "__main__":
    app.run(debug=True)
