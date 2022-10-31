from flask import Flask, render_template
from database.dbManager import return_dull_db_select    # todo()

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def main_page():
    data = return_dull_db_select()  # todo()
    return render_template('main.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
