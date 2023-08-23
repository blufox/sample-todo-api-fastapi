from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

#Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#Get single todos
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "no todos"}

#Create todos
@app.post("/todos")
async def store_todo(todo: Todo):
    todos.append(todo)
    return {"message" : "todo added"}

#Update todos
@app.get("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_object.item
            return {"todo": todo}
    return {"message": "no todos"}

#Delete todos
@app.get("/todos/{todo_id}")
async def destroy_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "todo deleted"}
    return {"message": "no todos"}