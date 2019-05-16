from flask import Flask, request, redirect, render_template
import cgi
import os
#import jinja2

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    #template = jinja2_env.get_template('hello_form.html')
    #return template.render()
    return render_template('hello_form.html')

    
@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    #template = jinja2_env.get_template('hello_greeting.html')
    #return template.render(name=first_name)
    return render_template('hello_greeting.html', name=first_name)


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

@app.route('/validate-time')
def display_time_form():
    #template = jinja2_env.get_template('time_form.html')
    #return template.render()
    return render_template('time_form.html')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route('/validate-time', methods=['post'])
def validate_time():

   hour = request.form['hour']
   minutes = request.form['minutes']

   hour_error = ''
   minutes_error = ''

   if not is_integer(hour):
       hour_error = 'Not a valid integer'
       hour = ''
   else:
        hour = int(hour)
        if hour > 23 or hour < 0:
            hour_error = 'Hour value out of range (0-23)'
        hour = ''

   if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
   else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

   if not minutes_error and not hour_error:
       time = str(hour) + ':' + str(minutes)
       return redirect('/valid-time?time={0}'.format(time)) #jhkjhjkh
   else:
       #template = jinja2_env.get_template('time_form.html') 
       return render_template('time_form.html', hour_error=hour_error, 
                minutes_error=minutes_error, hours= hour, minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)

tasks = [] 
@app.route('/todos', methods=['POST', 'GET'])
def todos():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    #template = jinja2_env.get_template('todos.html')
    #return template.render(title = 'TODOs', Stasks=tasks)
    return render_template('todos.html', title = 'TODOs', Stasks=tasks)
app.run()


