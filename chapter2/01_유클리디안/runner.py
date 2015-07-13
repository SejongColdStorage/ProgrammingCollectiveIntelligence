# coding=utf-8

from math import sqrt
from chapter2.recommendations import critics


# person1과 person2의 거리기반 유사도 점수를 리턴
def sim_distance(prefs, person1, person2):
    # # 공통 항목 목록 추출
    # si = {}
    # for item in prefs[person1]:
    #     if item in prefs[person2]:
    #         si[item] = 1
    #
    # # 공통항목이 없을 경우 0을 리턴
    # if len(si) == 0: return 0
    #
    # print(si)

    # 모든 차이 값의 제곱을 더함
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sqrt(sum_of_squares))

# 유클리디안 계산 결과 계산하기
result = sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
print(result)
