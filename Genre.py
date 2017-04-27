import tmdbsimple as tmdb
import json as json
import pandas as pd
import time as time
import os

KEY = os.environ['TMDB_API']
tmdb.API_KEY = str(KEY)


genre = tmdb.Genres()
search = tmdb.Search()
test = genre.list()
genres = test['genres']
tv_shows_array = ['content_title']

df=pd.read_csv('tvnames.csv', skipinitialspace=True, usecols=tv_shows_array)

tv_shows = df.content_title

tv_shows = df.values
f1=open('./good_genre.csv', 'w+')
f2=open('./bad_genre.csv', 'w+')
genre_list = {}


for j in genres:
	id = j['id']
	name = j['name']
	genre_list[id]=name

genre_list[10763] = 'News'
genre_list[10764] = 'Reality'
genre_list[10765] = 'Sci-fi & Fantasy'

for tv in tv_shows:
	response = search.tv(query=tv)
	time.sleep(.33)
	for s in search.results:
		y = s['genre_ids']
		tv_genre = []
		for x in y:
			if x not in genre_list:
				f2.write(str(x) + '\n')
				continue
			else:
				tv_genre.append(genre_list[x])
				if len(tv_genre) == 0:
					print("NO GENRE")
					for tv in tv_shows:
						response = search.movie(query=tv)
						time.sleep(.33)
						for s in search.results:
							y=s['genre_ids']
							for x in y:
								if x not in genre_list:
									f2.write(str(x) + '\n')
									continue
								else:	
									tv_genre.append(genre_list[x])
									print('This was from the Movie Database') 	
		final = s['name'],tv_genre
		print(final)
		f1.write(str(final) + '\n')



