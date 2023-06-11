from flask import Flask, render_template, abort
import random
from model.country import db, find_by_name, find_by_index

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


colors = {
    1: "red",
    2: "blue",
    3: "green"
}


@app.route('/color')
def random_color():  # lab example
    return str(colors.get(random.randint(1, 3)))


@app.route('/hello-world')
def hello_world_html():
    return render_template('welcome.html', message='Aplikacje Server side są super!')


@app.route('/countries')
def random_country():
    country_index = random.randint(0, 246)
    country = db[country_index]

    return render_template('country.html', country=country)


# path variable: <>typ:nazwa>
@app.route('/countries/<name>')
def country_by_name(name: str):
    try:
        found_country = find_by_name(name)
    except ValueError as ex:
        abort(404, ex)
    return render_template('country.html', country=found_country)


# podejemy inta - idzie do innego end pointa
@app.route('/countries/<int:name>')
def other_func(name: int):
    return str(name)


# mini lab2
@app.route('/countries/byindex/<int:index>')
def country_by_id(index: int):
    try:
        found_country = find_by_index(index)
    except IndexError:
        abort(404, f"Country by index {index} cannot be found")
    return render_template('country.html', country=found_country)


# podgląd mappingów
print(app.url_map)

if __name__ == '__main__':
    app.run()
