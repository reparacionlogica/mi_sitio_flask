from flask import Blueprint, render_template, request

bp = Blueprint("main", __name__)

@bp.get("/")
def home():
    return render_template("index.html", title="Inicio")

@bp.get("/about")
def about():
    return render_template("about.html", title="Acerca de")

@bp.get("/contact")
def contact_get():
    return render_template("contact.html", title="Contacto")

@bp.post("/contact")
def contact_post():
    nombre = request.form.get("nombre", "")
    email = request.form.get("email", "")
    mensaje = request.form.get("mensaje", "")
    # Aquí podrías guardar en DB o enviar un correo.
    return render_template("contact.html", title="Contacto",
                           enviado=True, nombre=nombre)
