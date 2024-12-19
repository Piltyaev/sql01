# Flask - самый простой

from flask import Flask

from sql_practice import add_post, get_posts, delete_post, get_post, update_post

# Создание объекта Flask - создали приложение
app = Flask(__name__)

weather = {"astana": -10.3, "almaty": -6.7, "vienna": 0}


@app.route("/")
def welcome():
    return "Abobus"


todos = []


@app.route("/name")
def get_name():
    return "Marlenlox"


# 1. Добавление поста
@app.route("/posts/add/<post_title>/<post_content>")
def add_new_post(post_title, post_content):
    return add_post(post_title, post_content)


# 2. Получить все посты
@app.route("/posts")
def get_all_posts():
    return get_posts()


# 3. Удаление поста по post_id
@app.route("/posts/delete/<post_id>")
def delete_post_by_id(post_id):
    return delete_post(post_id)


# 4. Обновление поста по post_id
@app.route("/posts/update/<post_id>/<new_title>/<new_content>")
def update_post_by_id(post_id, new_title, new_content):

    return update_post(post_id, new_title, new_content)


if __name__ == "__main__":
    app.run(port=5006, host="0.0.0.0", debug=True)
