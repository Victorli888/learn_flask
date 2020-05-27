# Create App
from flask import Flask
app = Flask(__name__)


def factors(num):
    return [x for x in range(1, num+1) if num % x == 0]


# Specify URL
@app.route('/hello/<name>')
# What the URL will return
def hello_name(name):
    return "Why hello there " + name


# URL for a different route
@app.route('/ey')
def eylmao():
    return "eylmao"


# URL route for finding the factors of a number using a previously defined method
@app.route('/factors/<int:num>')
def factors_route(num):
    return f"The factors for {num} are {factors(num)}"


# using a function to write /factors/<int:num> app
@app.route('/brute_factor/<int:num>')
def factors_display_raw_html(n):
    factors_list = factors(int(n))
    html = f"<h1> The factors of {n} are </h1> \n <ul>"

    # For each factor, we make a <li> item for it
    for f in factors_list:
        html += f"<li> {str(f)} </li> \n"
    html += "</ul> </body>"
    return html



# Run APP
if __name__ == '__main__':
    app.run(host='0.0.0.0')
