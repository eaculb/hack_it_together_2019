# Carry-On Caring (JetBlue Project)
_hack_it_together_2019_

_* note that any changes made after March 3rd were post-hackathon *_
_* customer side of the app *_

### Tools Used:
  * Python + Flask
  * Jinja2
  * HTML + Bootstrap 4
  * MongoDB

### Post-Hackathon:
  * Updates' Goal: Finish what we started , increase funcitonality, and learn more
  * Requirements:
    - Python 3.7 + virtual environment
    - Python libraries: flask, flask-pymongo, Flask-Bootstrap4, flask_mongoengine
    ```
    $ pip install requirements.txt
    ```
    - Files:
      + `config.py`: 
      ```
      mongoDBURL = "MONGODB URL HERE"
      flightID = "FLIGHT ID NUMBER HERE"
      secretKey = "SECRET KEY HERE"
      ```

#### Homepage:
  * Minimalist
  * Links to other pages available

#### Pages in General:
  * Navigation bar with current-page highlighting
  * Same minimalist look
  * Individualized messages in the navigation bar

#### Flight Info:
  * Information regarding the flight (flight and seat number, destimation, destination and estimated arrival time)
    - Flight number, destination, and arrival time need to be created on the database (don't have access to it) but variables are set for when they are created

#### Customer Satisfaction Survey:
  * Best way to improve is to get feedback from your customers
  * Questions: likelihopod of flying again with JetBlue, overall satisfaction, enjoyment of inflight snacks, crewmembers likeness, and other

#### Request Assistance:
  * Lists the inflight snacks, drinks and purchasable items and allows the customer to check which ones they want
  * Other: requests that don't fit the above categories (questions, barf bag, etc ...)
  * Allows for crew members' jobs to be easier and more time efficient given that it eliminates extra trips they would have to do other wise
  * Allows for customers to order items from their seats without raising hands or calling the crew members over.


### Original Plan: 
User will log into the wifi provided by JetBlue. Once they log in, they will be automatically redirected to Carry-On Caring page. They will be prompted to provide flight confirmation number and then will be redirected to a personalized website


#### 1. Check-up:
  * Will include:
    - Flight number
    - Ability to call the attendants
    - Drop down menu: Water, Food, and Other

#### 2. Cabin Crew Info:
  * Pilot and Flight Attendants:
    - Name
    - Langauges
      - Idea: If you know oen of the crew member speaks the same language as you, you would knwo you can communicate with them with ease and select them to assit you within the 'Request Assistance' page
    - Hometown
    - Fun facts
      - Idea: Curious about the fact? Talk to them!
    - Photo
