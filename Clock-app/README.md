Mission Overview
Clock App (clock_app):

Displays the current time.
Exposes an API endpoint (/update_time) to decrement the time.
Button App (button_app):

Contains a button to decrement the time.
Communicates with the clock_app by making a POST request to the /update_time API endpoint.

Step-by-Step Guide
Clone the Repository:

Create Flask Apps:

Create two directories: clock_app and button_app.
In each directory, create the necessary Python files (app.py) and templates.
clock_app: Displays the current time and updates it upon API request.
button_app: Contains a button to decrement the time and communicates with clock_app.
Set up the requirements.txt file in each directory.
Create Dockerfiles:

In each app directory, create a Dockerfile specifying the Docker image configuration.
Create Docker Compose File:

Create a docker-compose.yml file in the project root.
Define services for both clock_app and button_app, specifying build contexts and ports.
Configure a network for communication between the two containers.
Build and Run the Containers:

docker-compose up --build

Access the Apps:

The clock_app is available at http://localhost:5001.
The button_app is available at http://localhost:5002.
Notes
The button_app communicates with the clock_app using the requests library.
Ensure that the CLOCK_APP_URL environment variable in the button_app matches the URL where the clock_app is running in the Docker network.
