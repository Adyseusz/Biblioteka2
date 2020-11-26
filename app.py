from flask import Flask, render_template, request
from data_management import add_author, get_all_authors
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route("/dodaj_autora/", methods=['GET', 'POST'])
def dodaj_autora():
    if request.method == 'POST':
        imie = request.form['imie']
        nazwisko = request.form.get('nazwisko')
        add_author(imie, nazwisko)
    a = render_template('dodaj_autora.html')
    return a

@app.route("/wyswietl_autora/")
def wyswietl_autora():
    authors = get_all_authors()
    a = render_template('wyswietl_autora.html', authors=authors)
    return a


if __name__ == '__main__':
    app.run()
