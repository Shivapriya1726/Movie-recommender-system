# Movie-recommender-system
I have built a content-based movie recommender system on the Netflix movies data set. I have used Flask for the backend and deployed it


# Content-based movie recommender system: 
Content-based movie recommender system uses the attributes like cast, director, genre, rating and etc to recommend the movie to the user

# Steps:

1. Data collection: I have used this data set from Kaggle for this model development - https://www.kaggle.com/datasets/shivamb/netflix-shows
2. Data cleaning: For this movie recommender system I used only the movies data and removed the TV shows data and did some basic cleaning in the data
3. Data Transformation: In data transformation I used TfidfVectorizer. It is a popular text feature extraction method in natural language processing (NLP) that is used to convert a collection of text documents into a matrix of term-frequency-inverse document frequency (TF-IDF) features.
4. Similarity Calculation: I calculated the cosine similarity between every other row. 
5. Development: For Backend, I used flask to run the app and for the front end I used HTML and CSS.  


# API
To get the images for the movie poster I have used https://www.omdbapi.com/apikey.aspx 

# Demo of the project

https://user-images.githubusercontent.com/90460346/235072837-d50c9160-32ee-4a54-9053-f1b67111bda0.mp4


