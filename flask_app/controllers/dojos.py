from flask import render_template, request, redirect, url_for
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

@app.route("/dojos")
def index():
    # call the get all classmethod to get all dojos
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)

# READ/GET method, one record
@app.route("/dojos/<int:dojo_id>")
def show_one(dojo_id):
    # calling the get_one method and supplying it with the id of the dojo we want to get
    dojo = Dojo.show_one(dojo_id)
    # Retrieve all ninjas associated with the dojo
    ninjas = Ninja.get_ninjas_by_dojo(dojo_id)
    # passing one dojo to our template so we can display them
    return render_template("show.html", one_dojo = dojo, ninjas = ninjas)

# CREATE
# "Add Ninja"
@app.route('/ninjas')
def create():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

# "Add Dojo"
@app.route('/dojos/add', methods=['POST'])
def add():
    Dojo.add(request.form)
    return redirect('/')