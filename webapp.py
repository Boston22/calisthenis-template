from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')


def process_h():
    if  100 < h < 120:
        fitIndex + 5

def process_w():
    if 250 < w <300:
        fitIndex - 10

def process_a():
    if 0 < age < 7:
        fitIndex - 7

    elif 8 < age < 12:
        fitIndex - 12

    elif 13 < age < 17:
        fitIndex + 75

    elif 18 < age < 30:
        fitIndex + 100

    elif 31 < age < 41:
        fitIndex + 15

    elif 42 < age < 50:
        fitIndex + 7

    elif 51 < age < 70:
        fitIndex - 35

    elif 71 < age < 95:
        fitIndex - 50

    elif age >=95:
        fitIndex - 100

def process_t():
    if type == "slim":
        fitIndex + 70

    elif type == "fit":
        fitIndex + 45

    elif type == "built":
        fitIndex + 20


def process_c():
    if 0 <  < 10

def process_s():
    if 0 <  < 10

def process_f():
    if 0 <  < 10






def process_index():
    if fitIndex < 20 :
        "Yo uneed to work out a lot"
    if fitIndex > 80:
        "Here are some specific workouts to do"


@app.route("/r")
def render_response():
    global height
    global weight
    global age
    global type
    global choice
    global sex
    global forced
    global fitIndex
    fitIndex = 0
    height = int(request.args['Height'])
    weight = int(request.args['Weight'])
    age = int(request.args['Age'])
    type = request.args['Type']
    choice = request.args['Choice']
    sex = request.args['Sex']
    forced = request.args['Force']











    return render_template('response.html', different1 = render_variables())

if __name__=="__main__":
    app.run(debug=True)
