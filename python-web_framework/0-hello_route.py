# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and assign it to the 'app' variable
app = Flask(__name__)

# Define a route for the root URL ('/') and associate it with the hello_hbnb function
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    # Start the Flask development server on 0.0.0.0 (all available network interfaces) and port 5000
    app.run(host='0.0.0.0', port=5000)

