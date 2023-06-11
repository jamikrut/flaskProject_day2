from flask import Flask, render_template, abort, url_for
import random
from model.country import db, find_by_name, find_by_index, find_continent_by_cc, continent_map

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'white',
    5: 'orange',
    6: 'yellow',
    7: 'purple'
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


@app.route('/squares')
def squares_page():
    color1 = colors.get(random.randint(1, 7))
    color2 = colors.get(random.randint(1, 7))
    color3 = colors.get(random.randint(1, 7))
    color4 = colors.get(random.randint(1, 7))
    color5 = colors.get(random.randint(1, 7))
    color6 = colors.get(random.randint(1, 7))
    color7 = colors.get(random.randint(1, 7))
    color8 = colors.get(random.randint(1, 7))
    color9 = colors.get(random.randint(1, 7))
    return render_template('box.html', color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                           color6=color6, color7=color7, color8=color8, color9=color9)


# podgląd mappingów
print(app.url_map)

if __name__ == '__main__':
    app.run()
