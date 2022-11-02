from flask import Flask, render_template, request, redirect
from database.dbManager import DatabaseManager

app = Flask(__name__, template_folder='./templates')
dbm = DatabaseManager()
def contact():
    print('lmaop')

@app.route('/')
def main_page():
    data = dbm.select_all()
    return render_template('main.html', data=data)


@app.route("/delete", methods=["GET", "POST"])
def delete_page():
    if request.method == 'POST':
        delete_id = request.form.get('delete_row', 'none')
        try:
            delete_id = int(delete_id)
        except:
            return redirect(request.path)
        dbm.delete_by_id(delete_id=delete_id)
        return redirect(request.path)
    if request.method == "GET":
        data = dbm.select_all()
        return render_template('delete.html', data=data)


@app.route('/select')
def select_page():
    select_hash = request.args.get('select_hash', 'none')
    try:
        select_hash = int(select_hash)
        data = dbm.select_by_hash(hash_value=select_hash)
    except:
        data = dbm.select_all()
    return render_template('select.html', data=data)




@app.route("/update", methods=["GET", "POST"])
def update_page():
    if request.method == 'POST':


        try:
            update_id = request.form['update_id']
            update_name = request.form['update_name']
            update_desc = request.form['update_desc']
            update_hash = request.form['update_hash']

            if update_id != '':
                try:
                    update_id = int(update_id)
                except:
                    return redirect(request.path)
            else:
                return redirect(request.path)

            if update_name == '':
                update_name = None

            if update_desc == '':
                update_desc = None

            if update_hash != '':
                try:
                    update_hash = int(update_hash)
                except:
                    return redirect(request.path)
            else:
                update_hash = None

            if not(update_name or update_desc or update_hash):
                return redirect(request.path)

            dbm.update_row(update_id, update_name, update_desc, update_hash)

        except:
            pass
        return redirect(request.path)



    if request.method == "GET":
        data = dbm.select_all()
        return render_template('update.html', data=data)


@app.route("/insert", methods=["GET", "POST"])
def insert_page():
    if request.method == 'POST':
        try:
            insert_name = request.form['insert_name']
            insert_desc = request.form['insert_desc']
            insert_hash = request.form['insert_hash']
            if insert_hash != '':
                try:
                    insert_hash = int(insert_hash)
                except:
                    return redirect(request.path)
            else:
                insert_hash = None
            dbm.insert_row(ins_name=insert_name, ins_desc=insert_desc, ins_hash=insert_hash)

        except:
            pass
        return redirect(request.path)

    if request.method == "GET":
        data = dbm.select_all()
        return render_template('insert.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
