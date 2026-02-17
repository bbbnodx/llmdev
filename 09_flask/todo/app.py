from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


def load_todos() -> list:
    """ファイルからTODOリストを読み込む関数"""
    try:
        with open("todos.txt", "r") as file:
            todos = [line.strip() for line in file]
    except FileNotFoundError:
        todos = []

    return todos


def save_todos(todos: list) -> None:
    """TODOリストをファイルに保存する関数"""
    with open("todos.txt", "w") as file:
        file.write("\n".join(todos))


@app.route("/", methods=["GET", "POST"])
def index():
    todos = load_todos()
    if request.method == "POST":
        new_todo = request.form.get("todo")
        if new_todo:
            todos.append(new_todo)
            save_todos(todos)

        return redirect(url_for("index"))

    return render_template("index.html", todos=todos)


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todos = load_todos()
    deleted = todos.pop(todo_id)
    save_todos(todos)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
