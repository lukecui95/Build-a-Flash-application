# Project 2 -  Building on what you know about data - Pengwei Cui

This project is divided into two parts. 

The first part consists of a movies_tools.py file, a SI507_project2.py file and a movies_clean.csv file. The movies_tools.py file defined a class Movie, which was used to build the Flash application in SI507_project2.py. The SI507_project2.py file works as a Flash application, which allows you to go to the routes at some specific paths. Each of the routes depend upon the existence of movies_clean.csv.

The second part is a SI507_movies_database_plan database diagram, which represents some of the data in the movies_clean.csv file.
##First part 

### movies_clean.csv

The movies_clean.csv documented over 3000 movies in the cleaned format. It contains the movie title, US gross, director, IMDB Ratings and other information for each movies in the file.

### movies_tools.py

The movies_tools.py file defined a class Movie that accepts as constructor input one row of the movies_clean.csv file. It also contains a variable named num_records, which stores the number of movies records in the movies_clean.csv file. 

There are two methods in the movies_tools.py file.  

The first one is method “get_movies_ratings”. This method is used to get movie titles and their IMDB ratings. This method takes one parameter “num”, which indicates how many movies you want to get. We’ll use this method for the '/movies/ratings/' route in the Flask application. 

The second one is  method “get top rated movies”. This method is used to get five top rated movies. This method takes one parameter “num”, which is used to get movies with IMDB ratings greater than or equal to “num”. We’ll use this method for the '/movies/ratings/<rating>' route in the Flask application.



### SI507_project2.py

I created a Flash application in SI507_project2.py, which allows you to go to three specific routes, which means go to three different webs when you enter different URLs.

The first one is the homepage, which will display the number of movie records in our movies_clean.csv file. 

The second route is ‘/movies/ratings/’,  which will display a list of movies from the CSV data including their movie titles and IMDB ratings.

The third route is '/movies/ratings/<rating>', which enables you to get movies with IMDB ratings greater than or equal to <rating>. Please limit <rating> from 0 to 8.5, otherwise, it might take long time or forever to run the code.

### templates
There are two html files in the templates folder. These two html files are used to display contents for the second and third routes.


### How to run our Flash app
1) cd to the place you saved our files, and then type at the command prompt:
python SI507_project2.py runserver

2) Without doing anything else, in a web a browser, type in and check out this URL: "http://127.0.0.1:5000/" 

It should display:

3145 movies recorded



3) Change the ULR to " http://127.0.0.1:5000/movies/ratings/". This route will create an instance of the Movie class and use that instance to display the movie titles and IMDB ratings.

It should display (something like this):

Movie Title | IMBD rating :


American Desi | 6.7
Into the Blue | 5.7
Wallace & Gromit: The Curse of the Were-Rabbit | 7.9
United 93 | 7.8
Zathura | nan
War, Inc. | nan
BloodRayne | 2.7
Gun Shy | 5.4
King Kong | 7.6
Little Nicky | 5.0

 
4) Change the URL to "http://127.0.0.1:5000/movies/ratings/7.5". Actually, you can change 7.5 to any number from 0 to 8.5. 

It should display (something like this):

Five Movies with IMBD Rating greater than or equal to  7.5.



Movie Title | IMBD rating :


Religulous | 7.8
Super Size Me | 7.6
The Dress | 7.6
A Man for All Seasons | 8.1
Alien | 8.5

### Use requirements.txt to set your virtual environment

1) Create a virtual environment

python3 -m venv project2-env

2)Activate your virtual environment


source project2-env/bin/activate    # For Mac/Linux...
source project2-env/Scripts/activate    # For Windows

3)Install all requirements

pip install -r requirements.txt


4)Try our Flash app

See "How to run our Flash app"

5)Deactivate
deactivate

## Second Part

### SI507_movies_database_plan

This is a database diagram, which represents some of the data in the movies_clean.csv file.

I designed four tables in the diagram, which are Movie, Rating, Distributor and Director.
See details below:

![Test Image 6](https://github.com/lukecui95/SI507_Project2_cpengwei/blob/master/SI507_movies_database_plan.png)

