from application import app, db
from application.models import Tasks

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()
    output = ""
    for task in all_tasks:
        output += task.task_name + " " + task.task_description + " <br>" 
    return output


@app.route('/add/<name>')
def add(name):
    new_task = Tasks(task_name = name, task_description = 'new task')
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to To Do List"
 
@app.route("/delete/<int:id>")
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} is now delted"

@app.route('/update/<task_name>/<task_desc>')
def update(task_name, task_desc):
    task = Tasks.query.filter_by(task_name=task_name).first()
    task.task_description = task_desc
    db.session.commit()
    return f"Most recent task was updated with {task_desc}"

@app.route('/complete/<task_name>')
def complete(task_name):
    completed_task = Tasks.query.filter_by(task_name=task_name).first()
    completed_task.task_completion = True
    db.session.commit()
    return "The task has now been completed"

@app.route('/incomplete/<task_name>')
def incomplete(task_name):
    incompleted_task = Tasks.query.filter_by(task_name=task_name).first()
    incompleted_task.task_completion = False
    db.session.commit()
    return "The task is incomplete"