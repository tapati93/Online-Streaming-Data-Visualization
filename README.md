# Online-Streaming-Data-Visualization
Python, Kafka, MongoDB, Tableau


## IntroductionData source: TMDB 
TMDB is the collaborative database regarding movies and TV shows.
It contains more than 5000 movies and their rating and basic information, including user ratings and revenue data.

APIs:
GET/discover/movie{revenue}: Gets the list of m
GET/movie/{movie_id}: Gets the movie information based on the Movie ID.
GET/movie/{top_rated}: Gets the Top rated movies with all the relevant information.


## Problem Statement 1:
The Movie based streaming companies (Amazon Prime Video, Netflix. etc.) wants to identify the movies that the customers are very much interested to watch based on the Genre and Language. Also, they want to know the year in which maximum number of top-rated movies were released so that the companies can find out the public interest and stream those movies to increase the customers thereby increasing the company’s profit.



## Business Queries for Problem Statement 1
1. Which language has the highest ratings in our dataset?
2. In which year the highest and the lowest top-rated movies were released? What do you infer from the bar plot?
3. From our dataset, among which Genre the most and the least number of movies were released?

## Problem Statement 2:
A Production company wants to analyze a significant budget to produce a movie which results into a certain amount of profit. Also, they want to know if the total revenue is dependent on the Movie budget. 
## Business Queries for Problem Statement 2 
1. Which movie has the highest and lowest profit and budget in our dataset?
2. What are the top 20 movies w.r.t profit and budget?
3. What are the top 5 movie revenues w.r.t year?
4. What is the relationship between revenue and budget?


## Pipeline
![image](https://github.com/tapati93/Online-Streaming-Data-Visualization/assets/85105403/88b67436-7bfd-46d8-909c-df62020fee86)

## Difficulties:
1. Setting up of Kafka: Having no knowledge on this tool and difficulties in configuring Kafka.
2. Lack of Knowledge on the Kafka architecture to exchange the messages for data processing (Consumer and Producer). 
3. Difficulty in configuring the Kafka connector service in-order to enable the data transfer directly to the Database (MongoDB). 
4. Failure of connector service during bulk data transfer. 
5. Exhaustion of the API key after certain number of calls which exceeded the API calls limit. 	

## Decisions:
1. Going through the videos and the official websites related to “Aiven Kafka” to understand the configuration and it’s architecture. Pass the data to MongoDB through Kafka using Kafka producer. 
2. Transferring the data one after the other instead of bulk data transfer to avoid the Kafka connector service failure. 
3. Generation of new API key for accessing the data through that particular API. 	


## Conclusion


In the end, by visualizing our data we can conclude that one of the key features for movie’s success would be higher investment in the budget and to make more movies in Drama genre because from the visualization we understood that more budget leads to more revenue and also more people likes Drama based movies. We also see that the Drama genre in English language leads to more success in the movies because of its popularity. During the project we got a good opportunity to play around data with the help of functionalities like Kafka and Mongo DB. Python gave us a lot of flexibility with libraries like pandas and matplotlib to better visualize our data.





