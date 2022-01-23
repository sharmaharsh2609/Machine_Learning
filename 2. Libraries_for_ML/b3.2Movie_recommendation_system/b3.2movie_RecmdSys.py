#!/home/harsh/Machine_learning/ML_virtual_env/bin/python
#this above is path of my venv

# activate virtual environment before running this as I have installed all library packages inside my virtual environment 
import pandas as pd, warnings
warnings.filterwarnings('ignore') #ignore all the warnings from the output

df = pd.read_csv('/home/harsh/Machine_learning/Machine_learning/2. Libraries_for_ML/ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
df = df[['user_id', 'item_id', 'rating']] #we only need these 3 colas for now. remove others

df2 = pd.read_csv('/home/harsh/Machine_learning/Machine_learning/2. Libraries_for_ML/ml-100k/u.item', sep='\|', header=None, encoding='ISO-8859-1')
df2 = df2[[0,1]]  #select only these 2cols. remove everyone else.
df2.columns=['item_id', 'title']    # give headers for df2 dataframe which war not given in file.

df = df.merge(df2, on='item_id') #merge both the dataframes now.

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())  #df.groupby returns a series. So we convert it to dataframe also.
ratings['no of ratings'] = df.groupby('title')['rating'].count()  #add another column in ratings dataframe

movies = df.pivot_table(index='user_id', columns='title', values='rating')   #create movies array for all moviwe ratings by all users

def predict_movie(movie_name):
    movie_ratings = movies[movie_name]
    corr_movie = pd.DataFrame(movies.corrwith(movie_ratings))
    corr_movie.columns = ['correlation']
    corr_movie.dropna(inplace=True)   #Drop NaN values which has no correlation
    corr_movie = corr_movie.join(ratings['no of ratings'])
    
    predictions = corr_movie[corr_movie['no of ratings']>50].sort_values('correlation', ascending=False)
    
    return predictions.head(10)

#main program
movie=input("Enter any movie name from the all the movies given in u.item: ")  #movie name and spacing must be same
try:
    print("Top  10 movies similar to this movie with extent of similaarity and no of people who've watched is: \n", predict_movie(movie))
except:
    print("Some error occured! Try using exact same movie name and spacing as given in the u.item")