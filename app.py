from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    # Valores por defecto
    animal = "vacas"          # animal seleccionado por defecto
    cantidad = 0
    producto_total = 0.0
    precio_unitario = 0.0
    promedio = 0.0
    ingreso_total = 0.0

    if request.method == "POST":
        # Obtener el animal seleccionado
        animal = request.form.get("animal", "vacas")

        # Obtener y convertir los valores (con validación básica)
        try:
            cantidad = int(request.form.get("cantidad", 0))
        except ValueError:
            cantidad = 0

        try:
            producto_total = float(request.form.get("producto", 0))
        except ValueError:
            producto_total = 0.0

        try:
            precio_unitario = float(request.form.get("precio", 0))
        except ValueError:
            precio_unitario = 0.0

        # Evitar valores negativos
        if cantidad < 0:
            cantidad = 0
        if producto_total < 0:
            producto_total = 0.0
        if precio_unitario < 0:
            precio_unitario = 0.0

        # Calcular promedio solo si hay animales
        if cantidad > 0:
            promedio = producto_total / cantidad
        else:
            promedio = 0.0

        # Calcular ingreso total
        ingreso_total = producto_total * precio_unitario

    return render_template(
        "index.html",
        animal=animal,
        cantidad=cantidad,
        producto_total=producto_total,
        precio_unitario=precio_unitario,
        promedio=promedio,
        ingreso_total=ingreso_total
    )

if __name__ == "__main__":
    app.run(debug=True)