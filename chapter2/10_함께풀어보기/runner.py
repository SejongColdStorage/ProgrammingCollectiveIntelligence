__author__ = 'SejongPark'


from chapter2 import recommendations

prefs = recommendations.load_movie_lens('../movielens/')

user_sim = recommendations.calculate_similar_user(prefs)

print(user_sim)