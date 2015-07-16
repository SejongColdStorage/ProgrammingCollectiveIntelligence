__author__ = 'SejongPark'

from chapter2 import recommendations

item_sim = recommendations.calculate_similar_items(recommendations.critics)

print(item_sim)


result = recommendations.get_recommended_items(recommendations.critics, item_sim, 'Toby')

print(result)
