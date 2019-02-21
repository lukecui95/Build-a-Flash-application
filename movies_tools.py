
import pandas as pd
import random


movies_clean = pd.read_csv('movies_clean.csv')

class Movie:

    #Get the number of records in movies_clean.csv
    num_records = len(movies_clean)

    #Movie that accepts as constructor input one row of the movies_clean.csv file
    def __init__(self, movies_clean,i):
        self.title = movies_clean["Title"][i]
        self.US_gross = movies_clean['US Gross'][i]
        self.worldwide_gross = movies_clean['Worldwide Gross'][i]
        self.US_DVD_Sales = movies_clean['US DVD Sales'][i]
        self.production_budget = movies_clean['Production Budget'][i]
        self.release_date = movies_clean['Release Date'][i]
        self.MPAA_rating = movies_clean['MPAA Rating'][i]
        self.running_time = movies_clean['Running Time (min)'][i]
        self.distributor = movies_clean['Distributor'][i]
        self.source = movies_clean['Source'][i]
        self.major_genre = movies_clean['Major Genre'][i]
        self.creative_type = movies_clean['Creative Type'][i]
        self.director = movies_clean['Director'][i]
        self.rotten_tomatoes_ratings = movies_clean['Rotten Tomatoes Rating'][i]
        self.IMDB_rating = movies_clean['IMDB Rating'][i]
        self.IMDB_votes = movies_clean['IMDB Votes'][i]

    #Get movies and their IMDB ratings.
    def get_movies_ratings(self,num):
        movies_list = []
        for i in range(num):
            get_ratings = Movie(movies_clean,(i+random.randint(0,3134)))
            movies_list.append(get_ratings.title + '  '+'|'+'  ' + str(get_ratings.IMDB_rating))

        return movies_list

    #Get top rated movies.
    def get_top_rated(self,num):
        movies_list = []
        count = 0
        while count<5:
            get_ratings = Movie(movies_clean,(count+random.randint(0,3130)+random.randint(1,5)))
            if (get_ratings.IMDB_rating >= num):
                movies_list.append(get_ratings.title + '  '+'|'+'  ' + str(get_ratings.IMDB_rating))
                count = count + 1

        return movies_list


if __name__ == "__main__":
    pass

