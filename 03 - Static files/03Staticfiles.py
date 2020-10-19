from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

# Often, not all your data consists of Python files or HTML files. You might
# need CSS files, JavaScript files, images. For that, there is a static endpoint (folder in this case).
# From this folder you can call the files you need. Note that nothing is passed from
# this Python file; everything is done from within the HTML template.

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)