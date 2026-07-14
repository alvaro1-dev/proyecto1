from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------------
# MENÚ PRINCIPAL
# ------------------------
@app.route("/")
def inicio():
    return render_template("index.html")


# ------------------------
# EJERCICIO 1
# ------------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    promedio = None
    estado = None

    if request.method == "POST":

        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado
    )


# ------------------------
# EJERCICIO 2
# ------------------------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    nombre = None
    cantidad = None

    if request.method == "POST":

        n1 = request.form["nombre1"]
        n2 = request.form["nombre2"]
        n3 = request.form["nombre3"]

        mayor = max([n1, n2, n3], key=len)

        nombre = mayor
        cantidad = len(mayor)

    return render_template(
        "ejercicio2.html",
        nombre=nombre,
        cantidad=cantidad
    )


if __name__ == "__main__":
    app.run(debug=True)
