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






@app.route("/r")
def render_response():
    global height
    global weight
    global age
    global type
    global choice
    global sex
    global forced
    height = int(request.args['Height'])
    weight = int(request.args['Weight'])
    age = int(request.args['Age'])
    type = request.args['Type']
    choice = request.args['Choice']
    sex = request.args['Sex']
    forced = request.args['Force']
    h1 = request.args['height1']
    h2 = int(request.args['height2'])
    h3 = int(request.args['height3'])
    w1 = int(request.args['weight1'])
    w2 = int(request.args['weight2'])
    w3 = int(request.args['weight3'])
    w4 = int(request.args['weight4'])
    a1 = int(request.args['age1'])
    a2 = int(request.args['age2'])
    a3 = int(request.args['age3'])
    a4 = int(request.args['age4'])
    a5 = int(request.args['age5'])
    a6 = int(request.args['age6'])
    a7 = int(request.args['age7'])
    t1 = request.args['type1']
    t2 = request.args['type2']
    t3 = request.args['type3']
    c1 = request.args['choice1']
    c2 = request.args['choice2']
    f1 = request.args['force1']
    f2 = request.args['force2']










    return render_template('response.html', different1 = render_variables())

if __name__=="__main__":
    app.run(debug=True)
