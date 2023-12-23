from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '1234'

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        flash(f'Task "{task}" added to the to-do list.', 'success')

    def view_tasks(self):
        return self.tasks

    def remove_task(self, index):
        try:
            task = self.tasks.pop(index - 1)
            flash(f'Task "{task}" removed from the to-do list.', 'success')
        except IndexError:
            flash('Invalid task index. Please enter a valid index.', 'error')

todo_list = ToDoList()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        todo_list.add_task(task)

    tasks = todo_list.view_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/remove/<int:index>')
def remove_task(index):
    todo_list.remove_task(index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
