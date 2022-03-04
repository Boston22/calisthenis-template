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
    if height == 40 and weight == 150:
        rep15
    if weight == 50 and 100 < weight < 150:

    if 14 <= age <= 30 and 130 <= weight <= 160 and sex == Male:

    #if

    return dif1


@app.route("/r")
def render_response():
    height = int(request.args['Height'])
    weight = int(request.args['Weight'])
    age = int(request.args['Age'])
    bodyType = int(request.args['BodyType'])
    yourChoice = int(request.args['YourChoice'])
    sex = request.args['Sex']
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue

    #This is just for being here, look up actual ranges in inches.
    if 40 <= height or height <= 49:
        reply1 = "(input instructions)"
    if 50 <= height or height <= 59:
        reply2 = "(input instructions)"
    if 60 <= height or height <= 69:
        reply3 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    if 20 <= weight or weight <= 30:
        reply4 = "(input instructions)"
    if 40 <= weight or weight <= 50:
        reply5 = "(input instructions)"
    if 60 <= weight or weight <= 70:
        reply6 = "(input instructions)"
    if 80 <= weight or weight <= 90:
        reply7 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    if 14 <= age <= 30:
        reply8 = "Would reccomend doing calisthenics if you want to be in shape but not look like a gym addict."
    if 31 <= age <= 50:
        reply9 = "You can still do it and would reccomend if you are trying to look in shape."
    if 51 <= age <= 60:
        reply10 = "You can try it if you want to but only do it if you feel comfortable doing so."
    if 61 <= age <= 75:
        reply11 = "You probably shouldn't do it but if you are in good shape and have already started."
    if 76 <=  <= 85:
        reply12 = "Would not reccomend do to strain on body. If you do decide to then only do the base exercises that build the muscle needed to do calisthenics."
    if 86 <= age <= 100:
        reply13 = "Don't start doing calisthenics because it could be too strenuous on your body."
    if 101 <= age:
        reply15 = "HOW ARE YOU ALIVE?"

    #This is just for being here, look up actual ranges in inches.
    if 20 <= bodyType or bodyType <= 30:
        reply16 = "(input instructions)"
    if 20 <= bodyType or bodyType <= 30:
        reply17 = "(input instructions)"
    if 20 <= bodyType or bodyType <= 30:
        reply18 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    if 20 <= currentBody or currentBody <= 30:
        reply19 = "(input instructions)"
    if 20 <= currentBody or currentBody <= 30:
        reply20 = "(input instructions)"
    if 20 <= currentBody or currentBody <= 30:
        reply21 = "(input instructions)"


    #This is just for being here, look up actual ranges in inches.
    #if 20 = bodyType or bodyType <= 30:
        #reply19 = "(input instructions)"

    return render_template('response.html')
















    return render_template('response.html', response1 = reply1, response2 = reply2, response3 = reply3, response4 = reply4, response5 = reply5, response6 = reply6, response7 = reply7, response8 = reply8, response9 = reply9, response10 = reply10, response11 = reply11, response12 = reply12, response13 = reply13, response14 = reply14, response15 = reply15, response16 = reply16, response17 = reply17, response18 = reply18, response19 = reply19, response20 = reply20, response21 = reply21, different1 = dif1)

if __name__=="__main__":
    app.run(debug=True)
