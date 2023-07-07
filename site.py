from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
import git

app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line         # this gets the name of the file so Flask knows it's name
app.config['SECRET_KEY'] = 'afdd0fe598b149a59cb4c467259ea337'

@app.route("/")                          # this tells you the URL the method below is related to
#def hello_world():
    #return "<p>Hello, World! This page has nothing to show...</p>"        # this prints HTML to the webpage

@app.route("/home") 
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page UPDATED')

@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/kennyventress/seo_site_demo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
#@app.route("/register", methods=['GET', 'POST'])
#def register():
    #form = RegistrationForm()
    #if form.validate_on_submit(): # checks if entries are valid
        #flash(f'Account created for {form.username.data}!', 'success')
        #return redirect(url_for('home')) # if so - send to home page
    #return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")