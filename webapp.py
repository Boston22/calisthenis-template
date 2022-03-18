from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


def process_h(height): #height
    if  24 <= height <= 35:
        return + 100
    elif 36 <= height <= 47:
        return + 100
    elif 48 <= height <=59:
        return + 100
    elif 60 <= height <= 71:
        return + 90
    elif 72 <= height <= 83:
        return + 75
    elif 84 <= height <= 96:
        return + 75

def process_w(weight): #weight
    if weight <= 100:
        return - 100
    elif 101 <= weight <= 120:
        return + 50
    elif 121 <= weight <= 140:
        return + 50
    elif 141 <= weight <= 160:
        return + 100
    elif 161 <= weight <= 180:
        return + 85
    elif 181 <= weight <= 200:
        return + 75
    elif 201 <= weight <= 220:
        return - 10
    elif 221 <= weight <= 240:
        return - 25
    elif 241 <= weight <= 260:
        return - 50
    elif 261 <= weight <= 300:
        return - 75

def process_a(age): #age
    if 0 <= age <= 7:
        return - 50
    elif 8 <= age <= 12:
        return - 25
    elif 13 <= age <= 17:
        return + 75
    elif 18 <= age <= 30:
        return + 100
    elif 31 <= age <= 41:
        return + 15
    elif 42 <= age <= 50:
        return + 7
    elif 51 <= age <= 70:
        return - 35
    elif 71 <= age <= 90:
        return - 50
    elif age >=91:
        return - 100

def process_t(type): #type
    if type == "slim":
        return + 75
    elif type == "fit":
        return + 50
    elif type == "built":
        return + 25

def process_f(forced): #forced
    if forced == "yes":
        return - 100
    elif forced == "no":
        return + 100

def process_c(choice): #choice
    if choice == "yes":
        return + 100
    elif choice == "no":
        return - 100


@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():

    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')






# for inputting sex render_variables
# if 500 <= fitIndex <= 600 and male

# elif 601 <= fitIndex <= 700 and female




# final    def process_s():
#    if sex == male:


    #elif sex == female:



def process_index(sex): #what happens based on score from form
    if fitIndex <= 200 and sex == "male":
        "Do not do"
    elif fitIndex <= 200 and sex == "female":
        "Do not do"

    elif 201 <= fitIndex >= 300 and sex == "male":
        "Here are some specific workouts to do"
    elif 201 <= fitIndex >= 300 and sex == "female":
        "Here are some specific workouts to do"

    elif 301 <= fitIndex >= 400 and sex == "male":
        "fitIndex is between 301 and 400"
    elif 301 <= fitIndex >= 400 and sex == "female":
        "fitIndex is between 301 and 400"

    elif 401 <= fitIndex >= 500 and sex == "male":
        "fitIndex is between 401 and 500"
    elif 401 <= fitIndex >= 500 and sex == "female":
        "fitIndex is between 401 and 500"

    elif 501 <= fitIndex >= 600 and sex == "male":
        "fitIndex is between 501 and 600"
    elif 501 <= fitIndex >= 600 and sex == "female":
        "fitIndex is between 501 and 600"

    elif 601 <= fitIndex >= 700 and sex == "male":
        "fitIndex is between 601 and 700"
    elif 601 <= fitIndex >= 700 and sex == "female":
        "fitIndex is between 601 and 700"

    elif 701 <= fitIndex >= 800 and sex == "male":
        "fitIndex is between 701 and 800"
    elif 701 <= fitIndex >= 800 and sex == "female":
        "fitIndex is between 701 and 800"

    elif 801 <= fitIndex >= 900 and sex == "male":
        "fitIndex is between 801 and 900"
    elif 801 <= fitIndex >= 900 and sex == "female":
        "fitIndex is between 801 and 900"

    elif 901 <= fitIndex >= 1000 and sex == "male":
        "fitIndex is between 901 and 1000"
    elif 901 <= fitIndex >= 1000 and sex == "female":
        "fitIndex is between 901 and 1000"



@app.route("/r")
def render_response():
    global fitIndex
    fitIndex = 1000
    height = int(request.args['Height'])
    weight = int(request.args['Weight'])
    age = int(request.args['Age'])
    type = request.args['Type']
    choice = request.args['Choice']
    sex = request.args['Sex']
    forced = request.args['Force']
    process_h(height)
    process_w(weight)
    process_a(age)
    process_t(type)
    process_f(forced)
    process_c(choice)
    process_index(sex)

    return render_template('response.html', response1 = fitIndex)

if __name__=="__main__":
    app.run(debug=True)
