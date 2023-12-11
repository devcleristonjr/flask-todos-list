from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [
    {"name": "Sample Todo 1", "description": "This is a sample task 1.", "done": False},
    {"name": "Sample Todo 2", "description": "This is a sample task 2.", "done": True}
]


@app.route('/')
def index():
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    todos.append({'name': name, 'description': description, 'done': False})
    return redirect(url_for('index'))


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['name'] = request.form['name']
        todo['description'] = request.form['description']
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', todo=todo, index=index)


@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))


@app.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        todos.append({'name': name, 'description': description, 'done': False})
        return redirect(url_for('index'))
    return render_template('add_todo.html')




if __name__ == "__main__":
    app.run(debug=True)
