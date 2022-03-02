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
    return render_template('response.html')

@app.route("/r")
def render_response():
    height = int(request.args['Height'])
    weight = int(request.args['Weight'])
    age = int(request.args['Age'])
    bodyType = int(request.args['BodyType'])
    yourChoice = int(request.args['YourChoice'])
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
    if 20 <= weight or weight <= 30:
        reply5 = "(input instructions)"
    if 20 <= weight or weight <= 30:
        reply6 = "(input instructions)"
    if 20 <= weight or weight <= 30:
        reply7 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    if 10 <= age or age <= 20:
        reply8 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply9 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply10 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply11 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply12 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply13 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply14 = "(input instructions)"
    if 10 <= age or age <= 20:
        reply15 = "(input instructions)"

    #This is just for being here, look up actual ranges in inches.
    if 20 <= bodyType or bodyType <= 30:
        reply16 = "(input instructions)"
    if 20 <= bodyType or bodyType <= 30:
        reply17 = "(input instructions)"
    if 20 <= bodyType or bodyType <= 30:
        reply18 = "(input instructions)"


















    return render_template('response.html', response1 = reply1, response2 = reply2, response3 = reply3, response4 = reply4, response5 = reply5, response6 = reply6, response7 = reply7, response8 = reply8, response9 = reply9, response10 = reply10, response11 = reply11, response12 = reply12, response13 = reply13, responce14 = reply14, responce15 = reply15, responce16 = reply16, responce17 = reply17, responce18 = reply18, responce19 = reply19, responce20 = reply20, responce21 = reply21, responce22 = reply22, responce23 = reply23)

if __name__=="__main__":
    app.run(debug=True)
