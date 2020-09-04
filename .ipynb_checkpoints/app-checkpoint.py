# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
poo = Flask(__ClimateApp__)


# 3. Define what to do when a user hits the index route
@poo.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"
    


# 4. Define what to do when a user hits the /about route
@poo.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


@poo.route("/api/v1.0/stations")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@poo.route("/api/v1.0/tobs")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


@poo.route("/api/v1.0/<start>")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


@poo.route("/api/v1.0/<start>/<end>")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"





if __ClimateApp__ == "__main__":
    app.run(debug=True)