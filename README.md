<h1 align="center">--- WtW ---</h1>
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619659407/wtw_hero_huezqn.jpg" /></h1>

## :link:[ Live Website on Heroku](https://wtw-ms3.herokuapp.com/)

# About WtW (Or What to Watch (Or even Where to Watch)) 

You and your group of friends love movies and TV shows and you share the same kind of tastes. This is frequently the topic of conversation and you love recommending your lastest discoveries. As you love following their recommendations.

WtW is the best way to make this information available between yourselves at all times.You just need to add a cosy couch, some popcorn and 2 hours or so of quality free time.
 
## User Experience (UX)

All the design process was conducted with a simple purpose in mind: every single piece of information displayed on screen is a relevant one. 
This isn't a website ment to provide extensive data about the movies or tv shows, because there a lot of other pages that already do that very well. 
Instead, since the baseline of the presentation are the recommendations, the most part of the relevant data about the titles is accessible just by looking at the browse page, and the rest of it is reachable just by a single click. 
Apart from that, all the navigation and operations in the website are very easy since everything is layed out and styled in a way that you are already familiar with, and every menu or button are exactely where you expect them to be.

### User Stories

- #### Common user stories
    1. I want to intuitively navigate through the site to browse the content.
    2. I want to quickly get the information I'm looking for.
    3. I want to be able to view all titles listed.
    4. I want to be able to view all titles listed by me.
    5. I want to be able able to add a title recommendation.
    6. I want to be able able to edit a title added by me.
    7. I want to be able to search for a specific title name.
    8. I want to be able to search titles by type, genre, year of release or by the user who recommended it.
    9. I want to be able to contact the owner of the site.
    10. I want the page to be responsive on all screen sizes.

- #### As a first time visitor
    1. I want to be able to understand the purpose of the site.
    2. I want to be able to find the 'Register' page easily.
    3. I want to be able to register easily
    
- #### As a returning user
    1. I want to be able to easily find to the Log in page.
    2. I want to be able to know which recommendations I already listed.
    3. I want to be able to edit the recommendations I already listed.
    4. I want to be able to delete the recommendations I already listed.
    5. I want to be able to easily find the Log out button.

- #### As an admin
    1. I want to be able to add, edit or delete types of titles.
    2. I want to be able to add, edit or delete genres of titles.
    3. I want to be able to add, edit or delete platforms of titles.


### Design
Most of the design elements of this project were built using Google's Material Design inspired framework [Materialize](https://materializecss.com/), so everything feels very familiar as you've seen many of these elements in other places.

### Wireframes
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719355/MD%20Images/WtW_home_ALL_VIEWS_mjrnhu.jpg" /></h1>

The wireframes that layed out the ground for the design were made using Adobe's [XD](https://www.adobe.com/products/xd.html), even though some aspects were changed and adapted during development.
All the views can be accessed [here](./media/docs/wireframes.pdf) and checked bellow:

#### Mobile View
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719354/MD%20Images/wireframes_mobile_iranyb.jpg" /></h1>

#### Tablet View
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719354/MD%20Images/wireframes_tablet_duijlq.jpg" /></h1>

#### Desktop View
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719354/MD%20Images/wireframes_desktop_z5zdy0.jpg" /></h1>


#### Colours
Again, for a sense of familiarity, all the colours used are standard [Materialize](https://materializecss.com/) colours with some accents here and there for contrast purposes. The main theme colour is a Deep Purple (#6200ea), whilst in the titles' display cards you can find a light Indigo (#e8eaf6) as well as other variations of Purple. For the buttons, a combination of Reds, Teals and Blues were picked according to the button's functionality. 

#### Typography
The font chosen is Google's [Roboto](https://fonts.google.com/specimen/Roboto) as it allows letters to take up as much space as it needs and ultimately, making for an improved experience for the reader while looking very good in a wide range of devices.

#### Imagery
The only image in the current version of the website is the one in the home page, giving a warm welcome to the users while reinforcing the WtW branding. To achieve this result some image manipulation was done using Adobe's [Photoshop](https://www.adobe.com/products/photoshop.html)

#### Icons
To make the users' experience more pleasant and the navigation more intuitive a number of [Materialize](https://materializecss.com/)'s own icons were used, and in some specific cases I also recurred to [Font Awesome](https://fontawesome.com/).

## Features

This is a short description of the main features implemented in the project, and the main one left to implement.
 
### Existing Features
- **Responsiveness** - the whole website and its components adjust to the size of the screen
- **Navbar** - it's always displayed and allows users easily navigate through the website
- **Mobile Sidenav** - side menu navigation available on smaller devices and always available through 'hamburger' button
- **Sticky Footer** -  it's always at the bottom of the screen, no matter the amount of content displayed, and allows users to get in touch with the developer
- **Register account** - allows users to register their account having them fill out a user name and password
- **Session check** - When a user is logged in and tries to follow the register link it flashes a user already logged in message and routes him to Browse
- **Log in** - allows users to log in and have access to more functionalities
- **Password security** - passwords are salted and hashed using Werkzeug
- **Registered User Functionalites** - when a user is logged in he gains access to the Add and Edit tabs, and this allows them to post new title, change them and delete them. Edit and delete are only allowed if the title was created by the user in session
- **Admin User Functionalities** - when admin user is logged in he gains access to the Manage tabs, and this allows him to add, edit and delete title types, genres and platforms. Admin user can also edit or delete any title, even if it wasn't created by him
  - FOR EVALUTATION PURPOSES ONLY: to test admin functionalities you can use admin as login and adminadmin as the password
- **Search** - allows user to search the database for title name, type, genre, platform, year of release and the user who created the title
- **Search Index Update** - whenever a title is added, edited or deleted a new search index is created replacing the old one, so that search results are always up to date
- **Delete Confirmation Modal** - all delete operations pop up a modal confirmation dialog to avoid unwanted deletion of records
- **Card Reveal Functionalities** - in Browse, when users click the 3 dot icon the card reveals the recommendation text. Also, if the user is admin or the title is created by the same user, it reveals the edit and delete buttons.
- **404 Custom Page** - the website displays a custom designed page when it gets a 404 error
- **Custom Favicon** - the website displays a custom favicon in the browser tab 


### Features Left to Implement
- **Title Images** - retrieve title images from an API. This will have a huge impact in the UX as the title cards displaying the movies' covers will make the whole design more pleasing
- **Watch Here links** - retrieve the Whatch Here links from the database or ideally from an API. In the current version, if the user doesn't insert a correct link when adding a title it will hurt the UX
- **IMDB links** - retrieve IMDB links from the official API
- **Upgrade User Authentication** - add more security, password confirmation, more fields like email, profile picture, etc.
- **Overall UI/UX Fine Tune** - Add more images, transitions, animations, work on the styles and colours
- **User Profile Page** - where the users can change password, upload own photo, check messages, etc.
- **Messaging System** - where users can exchange messages with each other and admin 
- **Comments on title cards** - users can add additional comments to the existing recommendation of other users' titles

## Database 

This project uses MongoDB, which is a document-oriented NoSQL database used for high volume data storage. Instead of using tables and rows as in the traditional relational databases, MongoDB makes use of collections and documents. Documents consist of key-value pairs which are the basic unit of data in MongoDB. Collections contain sets of documents, which is the equivalent of relational database tables.
For WtW 5 collections were needed, which are as follows:
- **titles** - the main collection, used to store all the information required about the titles
- **title_types** - used to store the types of titles
- **genre** - used to store the genre of titles
- **platform** - used to store the platform of titles
- **user** - used to store the user login and hashed password information

Even though the database itself is non relational, some relations between documents in different collections have been made in the python app.
The following diagram details all the collections, its documents and their relations:
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719354/MD%20Images/database_model_whxrn4.jpg" /></h1>

## Technologies Used

In this section there is a list of all the technologies used to build this project.

- [HTML](https://dev.w3.org/html5/spec-LC/) - to build the templates.
- [Javascript](https://www.javascript.com/) - javaScript and JQuery initialize some Materialize components like modals and sidenav. 
- [Jquery](https://jquery.com/)
- [CSS](https://www.w3.org/Style/CSS/specs.en.html) - to add  aditional styling.
- [Materialize](https://materializecss.com/) - CSS & JS library and also icons.
- [FontAwesome](https://fontawesom.com/) - aditional icons not found in Materialize.
- [Python](https://www.python.org/) - primary backend language.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python framework for rendering templates, routing and connecting to DB.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) - library to allow to work with MongoDB from Python.
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Flask's templating language.
- [MongoDB](https://www.mongodb.com/) - non-relational database used to store user and project data.
- [DBdiagram.io](https://dbdiagram.io/) - for database design and modelling.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - for password security.
- [Gunicorn](https://gunicorn.org/) - a Python WSGI server.
- [BSON](http://bsonspec.org/) - to retrieve ObjectId in MongoDB from Python.
- [dnspython](https://dnspython.readthedocs.io/en/latest/) - a DNS toolkit for Python.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://github.com) - for cloud repository storage.
- [Heroku](https://heroku.com) - for deployment of production application.
- [Cloudinary](https://cloudinary.com/) - for online image storage.
- [VS Code](https://code.visualstudio.com/) - IDE of choice.
- [venv](https://docs.python.org/3/library/venv.html) - Python's built in virtual environment.
- [Adobe XD](https://www.adobe.com/products/xd.html) - for wireframes.
- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) - for image manipulation.
- [TIDAL](https://tidal.com/) - For countless hours of streamed Hi-Fi music. Couldn't have done it without this :musical_note: :satisfied::notes:

## Testing

 This section details all the testing that was made to ensure the good performance of the website.
 
 ### User Stories testing

 - #### Common user stories
    1. I want to intuitively navigate through the site to browse the content.
       - The navigation is clean and straightforward 
    2. I want to quickly get the information I'm looking for.
       - The Navbar is always accessible
       - In Browse all the title information is in the cards
       - In Add and Edit all the information is well displayed and the buttons intuitively placed
    3. I want to be able to view all titles listed.
       - I can in Browse
    4. I want to be able to view all titles listed by me.
       - I can in Edit
    5. I want to be able able to add a title recommendation.
       - I can in Add
    6. I want to be able able to edit a title added by me.
       - I can both in Browse and in Edit
    7. I want to be able to search for a specific title name.
       - I can in Browse
    8. I want to be able to search titles by type, genre, year of release or by the user who recommended it.
       - I can search by all these fields
    9. I want to be able to contact the owner of the site.
       - I have Linkedin and Github links in footer
    10. I want the page to be responsive on all screen sizes.
       - It is screen responsive

- #### As a first time visitor
    1. I want to be able to understand the purpose of the site.
       - The purpose is clear right in the landing/home page
    2. I want to be able to find the 'Register' page easily.
       - I have a call to action button in Home and a big button easy to see in navbar
    3. I want to be able to register easily
       - Just click Register button and fill 2 fields
    
- #### As a returning user
    1. I want to be able to easily find to the Log in page.
       - Login button is always present in navbar when no user session
    2. I want to be able to know which recommendations I already listed.
       - I can in Edit
    3. I want to be able to edit the recommendations I already listed.
       - I can in Browse and Edit
    4. I want to be able to delete the recommendations I already listed.
       - I can in Browse and Edit
    5. I want to be able to easily find the Log out button.
       - Log out button is always present in navbar when in user session

- #### As an admin
    1. I want to be able to add, edit or delete types of titles.
       - I can in Manage -> Types
    2. I want to be able to add, edit or delete genres of titles.
       - I can in Manage -> Genres
    3. I want to be able to add, edit or delete platforms of titles.
       - I can in Manage -> Platforms
 
 ### Manual Testing
 The following manual testing procedures were performed and concluded with success:

1. **Home page**:
   1. test navbar buttons
   2. test footer links
   3. test call to action button
      1. test browse button
      2. test register button
         1. test login link
            1. test register link
            2. test logging in
         2. test registering without meeting requirements
      3. test register button with session initiated to see if error is flashed
   4. test screen responsiveness
2. **Browse**:
   1. test search
      1. test search button
      2. test reset button
      3. try searching for title name
      4. try searching for type
      5. try searching for genre
      6. try searching for release year
      7. try searching for user name
   2. title cards
      1. compare information displayed with database
      2. check icon displayed for all_ages
      3. test imdb link
      4. test watch here link
      5. test screen responsiveness
      6. test card reveal functionality
         1. test edit title
         2. test delete title
            1. test delete confirmation cancel
            2. test delete confirmation confirm
   3. **Add**:
      1. test submiting without required fields
      2. test dropdown menu for type
      3. test dropdown menu for genre
      4. test dropdown menu for platform
      5. test all_ages toggle
      6. test submit button
      7. check if it adds to database
      8. test screen responsiveness
   4. **Edit**:
      1. check if titles displayed are all that were added by user in session
      2. compare information displayed with database
      3. check icon displayed for all_ages
      4. test imdb link
      5. test watch here link
      6. test screen responsiveness
      7. test card reveal functionality
      8. test edit title
         1. check if all information shows in the right fields
         2. test cancel button
         3. test save changes and compare to database
      9.  test delete title
          1.  test delete confirmation cancel
          2.  test delete confirmation confirm
   5.  **Manage**:
       1.  test manage types
           1. compare information displayed with database
           2. check add new button
              1. try submiting new and compare to database
              2. test back button
           3. test edit button
              1. check if field information is displayed
              2. test save changes
              3. test cancel edit 
           4. test delete button
              1. test delete confirmation cancel
              2. test delete confirmation confirm -> *here I got an error one time of not deleting the correct document, but I was not able to reproduce the error or find anything wrong with the code*
           5. test back button
       2.  test manage genres
           1. compare information displayed with database
           2. check add new button
              1. try submiting new and compare to database
              2. test back button
           3. test edit button
              1. check if field information is displayed
              2. test save changes
              3. test cancel edit 
           4. test delete button
              1. test delete confirmation cancel
              2. test delete confirmation confirm
           5. test back button
       3.  test manage platforms
           1. compare information displayed with database
           2. check add new button
              1. try submiting new and compare to database
              2. test back button
           3. test edit button
              1. check if field information is displayed
              2. test save changes
              3. test cancel edit 
           4. test delete button
              1. test delete confirmation cancel
              2. test delete confirmation confirm
           5. test back button
       4. check if menu displays with other user than admin
   6. **Log out**
      1. test logging out
      2. check if add, edit and manage are not displayed

### Code testing
The following tests were performed to the code:
#### Python PEP8 validation
Result: Met requirements.
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719354/MD%20Images/pep8_validation_vq6zjk.jpg" /></h1>

#### HTML W3C validation
Result: Tested all HTML files, and apart from Jinja related errors, no other errors were found.
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719355/MD%20Images/W3C_validation_zmofvt.jpg" /></h1>

#### CSS W3C validation
Result: No  errors found.
<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619734213/MD%20Images/CSS_W3C_validation_ztgmdj.jpg" /></h1>

### Lighthouse Performance testing
Result: The results vary a very small percentage from page to page, but are consistent within this variation. The Browse page on Heroku got a 95 Performance Rating.

<h1 align="center"><img src="https://res.cloudinary.com/djn4bzqse/image/upload/v1619719354/MD%20Images/lighthouse_score_uyidvc.jpg" /></h1>





 you need toIn convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This project was deployed locally while on development for testing purposes, and then deployedto Heroku for production mode.

### Local Deployment


These are the necessary steps for local deployment: 
1. Setup a virtual environment (not necessary but recommended) using the following command inside the project directory:
   ```
   python -m venv env
   ```
2. Activate the virtual environment using the following command:
   ```
   ./env/scripts/Activate.ps1
   ```
3. Install the requirements in the virtual environment:
   ```
   pip install -r requirements.txt
   ```
4. Create an env.py file to store environment variables:
   ```
   import os

   os.environ.setdefault("IP", "0.0.0.0")
   os.environ.setdefault("PORT", "5000")
   os.environ.setdefault("SECRET_KEY", "some,random,secret,key_not,the,one,in,here")
   os.environ.setdefault(
      "MONGO_URI", "mongodb,link,with,the,collection,name,and,access,data")
   os.environ.setdefault("MONGO_DBNAME", "name,of,the,collection")
   ```
6. Add env.py to the .gitignore so it won't get uploaded
5. Run the application:
   ```
   python app.py
   ```
6. Access the application in a browser tab:
   ```
   localhost:5000
   ```

### Heroku Deployment

These are the necessary steps for Heroku deployment: 

1. Create a Procfile with the following content:
   ```
   web: gunicorn app:app
   ```
   (Remember to remove whitespace and blank lines)
2. Log in to your [Heroku](https://id.heroku.com/login) account
3. Create a new app, name it and choose the appropriate region
4. Inside the app go to Settings
5. Click on Reveal Config Vars
6. Add each of the key value pairs, exactly the same as you have in the env.py file
7. Go to the Deploy tab 
8. Click on Github in Deployment Method and connect to your Github account
9. In Automatic Deploys search and select the correct Github repository, and then click on Enable Automatic Deploys
10. You can then click on Deply Branch, it takes a minute to build, and then you have the View button where you can open the deployed app.




## Credits

### Content
- [Stack Overflow](https://pt.stackoverflow.com/) was used numerous times to better understand and implement code

### Media
- The hero image was obtained from [The Telegraph](https://www.telegraph.co.uk/)
- The favicon was obtained from [favicon.cc](https://www.favicon.cc/)

### Acknowledgements

- The code logic was inspired by [Code Institute](https://codeinstitute.net/)'s Task Manager project

### Thank yous :pray:
- The developer community in general for the willingness to help others and making an infinite ammount of content available online and the Code Institute's Slack community in particular
- The numerous and too many to mention content creators that produce valuable guides an tutorials
- Code Institute Tutors for the precious insights in specific issues
- My Mentor Maranatha Ilesanmi for always pointing me to the right directio
