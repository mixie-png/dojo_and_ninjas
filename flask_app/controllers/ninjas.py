from flask import render_template, request, redirect, url_for
from flask_app.models.ninja import Ninja
# from flask_app.models.dojo import Dojo
from flask_app import app

# CREATE
# "New Ninja" form
@app.route('/ninjas/add', methods=['POST'])
def create_ninja():
    # Add a new ninja to the database
    Ninja.add(request.form)

    # Retrieve the associated dojo_id for the newly added ninja
    dojo_id = request.form['dojos']

    # Redirect to the show.html page for the specific dojo
    return redirect(url_for('show_one', dojo_id=dojo_id))