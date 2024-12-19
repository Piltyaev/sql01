from flask import Flask

app = Flask(__name__)

weather = {"astana": -10.3, "almaty": -6.7, "vienna": 0}


@app.route("/")
def welcome():
    return "Abobus"


@app.route("/name")
def get_name():
    return "Marlenlox"


@app.route("/city/<city_name>")
def weather_by_city(city_name):
    for city in weather:
        if city == city_name.lower():
            return f"В {city_name} {weather[city_name.lower()]} градусов по Цельсию"
    return f"Город {city_name} не найден"
    # return city_name


todos = []


@app.route("/todos/new/<title>")
def add_todos(title):
    todos.append(title)
    return "Задача добавлена в список!"


@app.route("/todos")
def print_todos():
    return todos


@app.route("/todos/remove/<index>")
def remove_element_of_todos(index):
    if todos.pop(int(index)) == -1:
        return "Удалять ничего нет"
    return todos


@app.route("/todos/edit/<index>/<new_title>")
def edit_element_of_todos(index, new_title):
    index = int(index)
    if -len(todos) <= index < len(todos):
        todos[index] = new_title
        return todos
    else:
        return "Index not found"


if __name__ == "__main__":
    app.run(port=5006, host="0.0.0.0", debug=True)
