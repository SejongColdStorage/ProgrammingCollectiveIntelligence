__author__ = 'SejongPark'

from chapter2 import recommendations

movies = recommendations.transform_prefs(recommendations.critics)

result1 = recommendations.top_matches(movies, 'Superman Returns')
result2 = recommendations.top_matches(movies, 'Superman Returns', 5, recommendations.sim_distance)

print(result1)
print(result2)
