__author__ = 'SejongPark'

from chapter2 import recommendations

prefs = recommendations.load_movie_lens('../movielens/')
print(prefs['87'])

item_sim = recommendations.calculate_similar_items(prefs, n=50)

result = recommendations.get_recommended_items(prefs, item_sim, '87')
print(result)
