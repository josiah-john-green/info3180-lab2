from app import app
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Josiah-John Green")


def format_date_joined(date):
    """Formats the given date as Month, Year."""
    return date.strftime('%B, %Y')


###
# The profile view function using the format_date_joined function
### 

@app.route('/profile/')
def profile():

    # Assuming you have a user with a 'date_joined' attribute
    user = {'username': 'Josiah-John Green', 'date_joined': datetime(2022, 2, 10)}

    # Use the format_date_joined function to format the date
    formatted_date = format_date_joined(user['date_joined'])

    return render_template('profile.html', name=user['username'], formatted_date=formatted_date)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
