from flask import Flask  # Import Flask to allow us to create our app
from flask import render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/anotherRoute')
def another_route():
    return 'You have hit another route'

@app.route('/users/<string:username>')
def user_name(username):
    return f"Welcome {username}!!!"

@app.route('/dashboard/<string:region>')
def dashboard(region):
    print(region)
    stacks = ['Python', 'Java', 'MERN']
    return render_template("index.html", region_code = region, stacks=stacks)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.