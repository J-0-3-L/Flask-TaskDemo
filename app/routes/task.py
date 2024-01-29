from flask import Blueprint, redirect, url_for, render_template, flash, request

from app import db

from app.models.task import Task


bp = Blueprint("task", __name__)


# LEER
@bp.route("/")
def index():
    tasks=Task.query.all()
    return render_template("index.html", tasks=tasks)


# CREAR
@bp.route("/create", methods=['POST'])
def create():
    task=Task(content=request.form['content'], done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("task.index"))

# ACCION
@bp.route("/done/<id>")
def done(id):
    task=Task.query.filter_by(id=int(id)).first()
    task.done=not(task.done)
    db.session.commit()
    return redirect(url_for("task.index"))


# ELIMINAR
@bp.route("/delete/<id>")
def delete(id):
    task=Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("task.index"))