from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    vacas = 0
    leche = 0
    precio = 0
    promedio = 0

    if request.method == "POST":
        vacas = int(request.form["vacas"])
        leche = float(request.form["leche"])
        precio = float(request.form["precio"])

        if vacas > 0:
            promedio = leche / vacas

    return render_template(
        "index.html",
        vacas=vacas,
        leche=leche,
        precio=precio,
        promedio=promedio
    )

if __name__ == "__main__":
    app.run(debug=True)