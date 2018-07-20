import automationhat
import time
from flask import Flask
app = Flask(__name__)

# Generate a simple HTML page. You could also use Flash's built-in Jinja Templating.
def makePage(body):
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>''' + body + '''
        <hr/>
        <ul>
            <li><a href="red">Red</a></li>
            <li><a href="yellow">Yellow</a></li>
            <li><a href="green">Green</a></li>
            <li><a href="off">All Off</a></li>
        </body>
    </html>
    '''

# This function runs every time a request is received before routing.
# We switch off all the lights here.
@app.before_request
def allOff():
    automationhat.output.one.off()
    automationhat.output.two.off()
    automationhat.output.three.off()

# Our default home page      
@app.route('/')
def index():
    return makePage('Index')

# The next three functions switch on the three lights
@app.route('/red')
def red():
    automationhat.output.one.on()
    return makePage('Red')

@app.route('/yellow')
def yellow():
    automationhat.output.two.on()
    return makePage('Yellow')

@app.route('/green')
def green():
    automationhat.output.three.on()
    return makePage('Green')

# Switch everything off
@app.route('/off')
def off():
    return makePage('Off')

# Let's announce ourselves by making the lights blink
automationhat.output.one.on()
time.sleep(0.2)
automationhat.output.one.off()
automationhat.output.two.on()
time.sleep(0.2)
automationhat.output.two.off()
automationhat.output.three.on()
time.sleep(0.2)
automationhat.output.three.off()

# Start the web server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0')
