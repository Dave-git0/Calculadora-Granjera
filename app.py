from flask import Flask, render_template, request

app = Flask(__name__)

# 🔹 Pantalla inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# 🔹 Calculadora
@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    animal = "vacas"
    cantidad = 0
    producto_total = 0.0
    precio_unitario = 0.0
    promedio = 0.0
    ingreso_total = 0.0

    if request.method == "POST":
        animal = request.form.get("animal", "vacas")

        try:
            cantidad = int(request.form.get("cantidad", 0))
        except:
            cantidad = 0

        try:
            producto_total = float(request.form.get("producto", 0))
        except:
            producto_total = 0.0

        try:
            precio_unitario = float(request.form.get("precio", 0))
        except:
            precio_unitario = 0.0

        if cantidad > 0:
            promedio = producto_total / cantidad

        ingreso_total = producto_total * precio_unitario

    return render_template(
        "calculadora.html",
        animal=animal,
        cantidad=cantidad,
        producto_total=producto_total,
        precio_unitario=precio_unitario,
        promedio=promedio,
        ingreso_total=ingreso_total
    )


# 🔹 Glosario
@app.route("/glosario")
def glosario():
    return render_template("glosario.html")


if __name__ == "__main__":
    app.run(debug=True)