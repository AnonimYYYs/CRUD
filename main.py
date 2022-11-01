from flask import Flask, render_template
from database.dbManager import return_dull_db_select    # todo()

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def main_page():
    data = return_dull_db_select()  # todo()
    return render_template('main.html', data=data)


@app.route('/delete')
def delete_page():
    data = return_dull_db_select()  # todo()
    return render_template('delete.html', data=data)


@app.route('/select')
def select_page():
    data = return_dull_db_select()  # todo()
    return render_template('select.html', data=data)


@app.route('/update')
def update_page():
    data = return_dull_db_select()  # todo()
    return render_template('update.html', data=data)


@app.route('/insert')
def insert_page():
    data = return_dull_db_select()  # todo()
    return render_template('insert.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
