from application import app, db
from application.models import Tasks
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()
    output = ""
    return render_template("index.html", title = "Home", all_tasks=all_tasks)

@app.route('/create', methods=["GET","POST"])
def create():
    form = TaskForm() 
    if request.method == "POST":
        new_task=Tasks(task_name=form.task_name.data, task_description=form.task_description.data, task_completion=False)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", title="Create a task", form=form)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = TaskForm()
    task = Tasks.query.filter_by(id=id).first()
    if request.method == "POST":
    #if form.validate_on_submit():
        task.task_description = form.task_description.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Task", task=task)

@app.route('/complete/<int:id>')
def complete(id):
    completed_task = Tasks.query.filter_by(id=id).first()
    completed_task.task_completion = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    incompleted_task = Tasks.query.filter_by(id=id).first()
    incompleted_task.task_completion = False
    db.session.commit()
    return redirect(url_for("home"))