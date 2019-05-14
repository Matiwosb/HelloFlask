from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

'''form ="""
# <!doctype html>
# <html>
    # <body>
        # <form action="/hello" method="post">
            <label for="first_name">First Name: </label>
            <input id="first_name" type="text" name="first_name"/>
            <input type="submit" />

        </form>
    <body>
<html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '<h1>'''

'''@app.route("/form-inputs")
def display_form_inputs():
    return """
    <style>
    br {margin-bottom: 20px;}
    </style>
    <form method='POST'>
        <label>type=text
            <input name="user-name" type="text" />
        </label>
        <br>
        <label>type=password
            <input name="user-password" type="password" />
        </label>
        <br>
        <label>type=email
            <input name="user-email" type="email" />
        </label>
        <br>
        <input name="shopping-cart-id" value="0129384" type="hidden" />
        <br>
        <label>Ketchup
            <input type="checkbox" name="cb1" value="first-cb" />
        </label>
        <br>
        <label>Mustard
            <input type="checkbox" name="cb2" value="second-cb" />
        </label>
        <br>
        <label>Small
            <input type="radio" name="coffee-size" value="sm" />
        </label>
        <label>Medium
            <input type="radio" name="coffee-size" value="med" />
        </label>
        <label>Large
            <input type="radio" name="coffee-size" value="lg" />
        </label>
        <br>
        <label>Your life story
            <textarea name="life-story"></textarea>
        </label>
        <br>
        <label>LaunchCode Hub
            <select name="lc-hub">
                <option value="kc">Kansas City</option>
                <option value="mia">Miami</option>
                <option value="ri">Providence</option>
                <option value="sea">Seattle</option>
                <option value="pdx">Portland</option>
            </select>
        </label>
        <br>
        <input type="submit" />
    </form>
    """


@app.route("/form-inputs", methods=['POST'])
def print_form_values():
    resp = ""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(
            key=field, value=request.form[field])
    return resp
app.run()'''

time_form = """
    <style>
        .error{{color: red;}}
    </style>
    <h1>Validate Time</h1>
    <form method = 'POST'>
        <label> Hours(24-four format)
            <input name="hour" type="text" value='{hours}'/>
        </label>
        <p class = "error">{hour_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}'/>
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Convert" />
    </form>"""


@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hour_error='',
        minutes='', minutes_error='')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route('/validate-time', methods=['post'])
def validate_time():

   hours = request.form['hour']
   minutes = request.form['minutes']

   hour_error = ''
   minutes_error = ''

   if not is_integer(hours):
       hour_error = 'Not a valid integer'
       hours = ''
   else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hour_error = 'Hour value out of range (0-23)'
        hours = ''

   if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
   else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

   if not minutes_error and not hour_error:
       time = str(hours) + ':' + str(minutes)
       return redirect('/valid-time?time={0}'.format(time))
   else:
       return time_form.format(hour_error=hour_error, 
                minutes_error=minutes_error, hours=hours, minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)
    

app.run()


