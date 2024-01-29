import pandas as pd

file = './DATA/movies.csv'
movies = pd.read_csv(file, index_col='Title')

movies['Gross'].str.replace(to_replace=['$, ,'], value = ['', ''], regex = False)
print(movies)