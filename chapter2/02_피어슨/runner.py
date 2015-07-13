# coding=utf-8
__author__ = 'SejongPark'

from chapter2 import recommendations
from math import sqrt


# p1과 p2에대한 피어슨 상관계수를 리턴
def sim_person(prefs, p1, p2):
    # 같이 평가한 항목들의 목록을 구함
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # 요소들의개수를 구함
    n = len(si)

    if n == 0:
        return 0

    # 모든선호도를 합산함
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # 제곱의 합을 계산
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # 곱의합을 계산
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 피어슨 점수 계산
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0: return 0

    r = num / den

    return r


def top_matches(prefs, person, n=5, similarity=sim_person):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()

    return scores[0:n]

# 피어슨 결과...
print(
    sim_person(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
)

# 평론가 순위 매기기
print(top_matches(recommendations.critics, 'Toby'))
