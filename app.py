from flask import Flask, render_template, request, redirect

app = Flask(__name__)

TASK_FILE = "tasks.txt"

def read_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return f.readlines()
    except:
        return []

def write_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.writelines(tasks)
@app.route("/")
def home():
    tasks = read_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task") + "\n"
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        write_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)