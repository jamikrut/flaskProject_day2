from flask import Flask, render_template, abort, url_for
import random
from model.country import db, find_by_name, find_by_index, find_continent_by_cc, continent_map
import pycountry_convert

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


# mini lab2
# podejemy inta - idzie do innego end pointa
@app.route('/countries/index/<int:index>')
def country_by_index(index: int):
    try:
        found_country = find_by_index(index)
        found_country['continent'] = find_continent_by_cc(found_country['cc'])
    except IndexError:
        abort(404, f"Country by index {index} cannot be found")
    return render_template('country_index.html', country=found_country, index=index, continent_map=continent_map)


# podgląd mappingów
print(app.url_map)

if __name__ == '__main__':
    app.run()
