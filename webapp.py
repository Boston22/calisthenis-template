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


def render_variables():
    if 40 <= height  <= 49 and weight == 150:
        dif1 = ""
        return dif1
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 40 <= height  <= 49 and 100 < weight < 150:
        dif2 = ""
    elif 50 <= height  <= 59 and 100 < weight < 150:
        dif2 = ""
        return dif2
    elif 60 <= height  <= 69 and 130 <= weight <= 160 and sex == Male:
        dif3 = ""
        return dif3
    elif 60 <= height <= 69 and 105 <= weight <= 124 and 14 <= age <= 30 and type == "slim" and sex == "male":
        dif4 = "this is test1"
        return dif4
    elif 60 <= height <= 69 and 105 <= weight <= 124 and 14 <= age <= 30 and type == "slim" and sex == "male" and choice == "yes" and forced == "no":
        dif12 = "this is test2"
        return dif12
    elif 70 <= height <= 79:
        dif5 = ""
        return dif5
    elif 80 <= height <= 89:
        dif6 = ""
        return dif6
    elif 105 <= weight <= 124:
        dif7 = ""
        return dif7
    elif 125 <= weight <= 149:
        dif8 = ""
        return dif8
    elif 150 <= weight <= 174:
        dif9 = ""
        return dif9
    elif 175 <= weight <= 200:
        dif10 = ""
        return dif10
    elif 14 <= age <= 30:
        dif11 = ""
        return dif11


    #return dif1, dif2, dif3, dif4, dif5, dif6, dif7,  dif8, dif9, dif10, dif11


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






    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue

    #This is just for being here, look up actual ranges in inches.
    #if 40 <= height or height <= 49:
    #    reply1 = "(input instructions)"
    #elif 50 <= height or height <= 59:
    #    reply2 = "(input instructions)"
    #elif 60 <= height or height <= 69:
    #    reply3 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    #if 105 <= weight or weight <= 124:
    #    reply4 = "(input instructions)"
    #elif 125 <= weight or weight <= 149:
    #    reply5 = "(input instructions)"
    #elif 150 <= weight or weight <= 174:
    #    reply6 = "(input instructions)"
    #elif 175 <= weight or weight <= 200:
    #    reply7 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    #if 14 <= age <= 30:
    #    reply8 = "Would reccomend doing calisthenics if you want to be in shape but not look like a gym addict."
    #elif 31 <= age <= 50:
    #    reply9 = "You can still do it and would reccomend if you are trying to look in shape."
    #elif 51 <= age <= 60:
    #    reply10 = "You can try it if you want to but only do it if you feel comfortable doing so."
    #elif 61 <= age <= 75:
    #    reply11 = "You probably shouldn't do it but if you are in good shape and have already started."
    #elif 76 <= age <= 85:
    #    reply12 = "Would not reccomend do to strain on body. If you do decide to then only do the base exercises that build the muscle needed to do calisthenics."
    #elif 86 <= age <= 100:
    #    reply13 = "Don't start doing calisthenics because it could be too strenuous on your body."
    #elif age > 100:
    #    reply15 = "HOW ARE YOU ALIVE?"

    #This is just for being here, look up actual ranges in inches.
    #if type == "Built":
    #    reply16 = "(input instructions)"
    #elif type == "Fit":
    #    reply17 = "(input instructions)"
    #elif type == "Slim":
    #    reply18 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    #if 20 <= currentBody or currentBody <= 30:
    #    reply19 = "(input instructions)"
    #if 20 <= currentBody or currentBody <= 30:
    #    reply20 = "(input instructions)"
    #if 20 <= currentBody or currentBody <= 30:
    #    reply21 = "(input instructions)"

    #if choice == "yes":
    #    rep22 = "t"
    #elif choice == "no":
    #    rep23 = "t"

    #elif forced == "yes":
    #    rep24 = "t"
    #elif forced == "no":
    #    rep25 = "t"
    #This is just for being here, look up actual ranges in inches.
    #if 20 = bodyType or bodyType <= 30:
        #reply19 = "(input instructions)"




    return render_template('response.html', different1 = render_variables())

if __name__=="__main__":
    app.run(debug=True)
