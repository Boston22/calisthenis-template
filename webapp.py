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


def process_h(): #height
    if  24 <= height <= 35:
        fitIndex = fitIndex + 100
    elif 36 <= height <= 47:
        fitIndex = fitIndex + 100
    elif 48 <= height <=59:
        fitIndex = fitIndex + 100
    elif 60 <= height <= 71:
        fitIndex = fitIndex + 90
    elif 72 <= height <= 83:
        fitIndex = fitIndex + 75
    elif 84 <= height <= 96:
        fitIndex = fitIndex + 75

def process_w(): #weight
    if weight <= 100:
        fitIndex = fitIndex - 100
    elif 101 <= weight <= 120:
        fitIndex = fitIndex + 50
    elif 121 <= weight <= 140:
        fitIndex = fitIndex + 50
    elif 141 <= weight <= 160:
        fitIndex = fitIndex + 100
    elif 161 <= weight <= 180:
        fitIndex = fitIndex + 85
    elif 181 <= weight <= 200:
        fitIndex = fitIndex + 75
    elif 201 <= weight <= 220:
        fitIndex = fitIndex - 10
    elif 221 <= weight <= 240:
        fitIndex = fitIndex - 25
    elif 241 <= weight <= 260:
        fitIndex = fitIndex - 50
    elif 261 <= weight <= 300:
        fitIndex = fitIndex - 75

def process_a(): #age
    if 0 <= age <= 7:
        fitIndex = fitIndex - 50
    elif 8 <= age <= 12:
        fitIndex = fitIndex - 25
    elif 13 <= age <= 17:
        fitIndex = fitIndex + 75
    elif 18 <= age <= 30:
        fitIndex = fitIndex + 100
    elif 31 <= age <= 41:
        fitIndex = fitIndex + 15
    elif 42 <= age <= 50:
        fitIndex = fitIndex + 7
    elif 51 <= age <= 70:
        fitIndex = fitIndex - 35
    elif 71 <= age <= 90:
        fitIndex = fitIndex - 50
    elif age >=91:
        fitIndex = fitIndex - 100

def process_t(): #type
    if type == "slim":
        fitIndex = fitIndex + 75
    elif type == "fit":
        fitIndex = fitIndex + 50
    elif type == "built":
        fitIndex = fitIndex + 25

def process_f(): #forced
    if forced == "yes":
        fitIndex = fitIndex + 100
    elif forced == "no":
        fitIndex = fitIndex - 100

def process_c(): #choice
    if choice == "yes":
        fitIndex = fitIndex + 100
    elif choice == "no":
        fitIndex = fitIndex - 100



# for inputting sex render_variables
# if 500 <= fitIndex <= 600 and male

# elif 601 <= fitIndex <= 700 and female




# final    def process_s():
#    if sex == male:


    #elif sex == female:



def process_index(): #what happens based on score from form
    if fitIndex <= 200 :
        "Do not do"
    elif 201 <= fitIndex => 300:
        "Here are some specific workouts to do"
    elif 301 <= fitIndex => 400:
        "fitIndex is between 301 and 400"
    elif 401 <= fitIndex => 500:
        "fitIndex is between 401 and 500"
    elif 501 <= fitIndex => 600:
        "fitIndex is between 501 and 600"
    elif 601 <= fitIndex => 700:
        "fitIndex is between 601 and 700"
    elif 701 <= fitIndex => 800:
        "fitIndex is between 701 and 800"
    elif 801 <= fitIndex => 900:
        "fitIndex is between 801 and 900"
    elif 901 <= fitIndex => 1000:
        "fitIndex is between 901 and 1000"


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
