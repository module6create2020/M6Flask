from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "There's nothing here. Try '/hardcoded', '/first_template', or '/second_template/<name>'"
# Below you see an example of hardcoding: programming without the possibility
# of any variability. This HTML cannot be changed using Flask or anything else.
# Not very useful...
@app.route('/hardcoded/')
def hardcoded_index():
    return '<html><body><h1>Hi, this is hardcoded HTML. BAD!</h1></body></html>'

# Instead, we can make use of templates. The .html files are in a subfolder "templates"
@app.route('/first_template')
def first_template():
    return render_template('first_template.html')

@app.route('/second_template/')
def second_template_no_name():
    return "No dummy, go to /second_template/some_name"

# To make use of the variables, let's use the second template:
@app.route('/second_template/<name>')
def second_template(name):
    return render_template('second_template.html', name=name)

@app.route('/third_template/')
def third_template_no_number():
    return "Enter a number after /third_template/"

# You can also use conditionals and other python code inside the template.
@app.route('/third_template/<int:number>')
@app.route('/third_template/<float:number>')
def third_template(number):
    return render_template('third_template.html', number=number)

dict = {"Apple": "Red", "Pear": "Green", "Tomato": "Red Again"}
@app.route('/fourth_template/')
def fourth_template():
    return render_template('fourth_template.html', dict=dict)


if __name__ == '__main__':
    app.run(debug=True)