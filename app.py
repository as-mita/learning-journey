from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
tasks = [
    {"id": 1, "task": "Learn API basics"},
    {"id": 2, "task": "Practice full-stack projects"}
]

# Home route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Simple Task API!"})

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Add a new task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    new_task = {
        "id": len(tasks) + 1,
        "task": data.get("task")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Delete a task by ID
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
