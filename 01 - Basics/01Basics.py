from flask import Flask, redirect, url_for
app = Flask(__name__)

# Below is a decorator, which binds a URL to a function. Here,
# www.helloworld.nl/ is bound to the hello_world() function.
@app.route('/')
def home():
    return "<h1> Hey! This is the root page!</h1>"

# In this example, you can pass any variable and it will be printed
# in the webpage. A multiline string is used to create some standard HTML
# and the curly brackets {} are used with the .format() function to insert
# the variable into those brackets later.
text_var_route = '''
    <h1>This is how you can pass variables into the URL:<br>
    Variable: {}</h1>
    <p> You could use this to access a blog with a specific ID by
    entering www.myblogsite.nl/blog/[blogID].
    '''
@app.route('/<variable_name>/')
def demo_var_url(variable_name):
    return text_var_route.format(variable_name)

# Here, you parse number (ints or floats) into the webpage through the URL.
# Note that for each there is a different converters: <int:variable> and <float:variable>.
# You can use this to use the input as numbers instead of strings.
# Additionally, two decorators (one for ints, one for floats) are linked to the same function.
text_demo_int = '''
                <h1>The number you entered was {0}.</h1>
                <p> Because it is
                passed as an {4} instead of a string, you can do
                calculations with them! Like:</p>
                <br>
                <ul>
                    <li>
                    The square of {0} is {1}!
                    </li>
                    <li>
                    {0} is between {2} and {3}.
                    </li>
                    <li>
                    You get the idea...
                    </li>
                </ul>
                <br>
                Finally, if you look into the source code, you can see that two decorators are attached
                <br> to the same function. This is called overloading.</p>
                '''
@app.route('/datatype/<float:number>/')
@app.route('/datatype/<int:number>/')
def demo_int(number):
    return text_demo_int.format(number, number**2, number-1, number+1, type(number).__name__)

# In this part you can see how you can redirect to other pages.
# Even better, you can do it conditionally. In the login() function.
# The name variable is check to see if it's "admin". If it is, forward
# the user to the login/admin page. Otherwise, forward the user to the
# login/user page. Note that the name is forwarded to the user page to
# be displayed there. And note that the argument in the url_for function is
# NOT the URL, but the FUNCTION name. Please make sure you import "redirect"
# and "url_for" from flask

@app.route('/login/guest/<username>/')
def user_page(username):
    return "You just got forwarded here, <b>{}</b>, because your not an admin.".format(username)

@app.route('/login/admin/')
def admin_page():
    return "Hello, admin!"

@app.route('/login/<name>/')
def login(name):
    if name == 'admin':
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('user_page', username=name))

if __name__ == '__main__':
    # Optional paramters: (host, port, debug, options).
    # Set debug=True as an argument to reload the code
    # each time the code is changed. Useful for development.
    app.run(debug=True)