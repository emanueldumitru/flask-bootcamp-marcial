from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vn.microsoft.icon')