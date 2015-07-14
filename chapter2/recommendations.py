# coding=utf-8
__author__ = 'SejongPark'

from math import sqrt

critics = {
    'Lisa Rose':
        {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
         'The Night Listener': 3.0},
    'Gene Seymour':
        {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
         'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
         'You, Me and Dupree': 3.5},
    'Michael Phillips':
        {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
         'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig':
        {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
         'The Night Listener': 4.5, 'Superman Returns': 4.0,
         'You, Me and Dupree': 2.5},
    'Mick LaSalle':
        {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
         'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
         'You, Me and Dupree': 2.0},
    'Jack Matthews':
        {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
         'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby':
        {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}
}


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

    if den == 0:
        return 0

    r = num / den

    return r


def top_matches(prefs, person, n=5, similarity=sim_person):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()

    return scores[0:n]


def get_recommataions(prefs, person, similarity=sim_person):
    totals = {}
    sim_sums = {}

    for other in prefs:
        # 나와 나는 비교하지않는다.
        if other == person:
            continue

        sim = similarity(prefs, person, other)

        # 0이하의 점수는 무시함
        if sim <= 0:
            continue
        for item in prefs[other]:
            # 내가 보지 못한 영화만 대상으로 한다.
            if item not in prefs[person] or prefs[person][item] == 0:
                # 유사도 * 점수
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                # 유사도 합계
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    # 정규화된 목록 생성
    rankings = [(total / sim_sums[item], item) for item, total in totals.items()]

    # 정렬된 목록 리턴
    rankings.sort()
    rankings.reverse()

    return rankings


def transform_prefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]

    return result
