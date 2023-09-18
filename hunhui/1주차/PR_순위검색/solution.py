from itertools import product
from bisect import bisect_left

languages = ['cpp','java','python']
roles = ['backend','frontend']
careers = ['junior','senior']
foods = ['chicken','pizza']

def make_keys(language, role, career, food):
    new_languages = [language] if language else languages
    new_roles = [role] if role else roles
    new_careers = [career] if career else careers
    new_foods = [food] if food else foods
    combinations = list(product(new_languages, new_roles, new_careers, new_foods))
    return ['|'.join(comb) for comb in combinations]

def solution(info, query):
    all_keys = make_keys(None,None,None,None)
    info_dict = {}
    for key in all_keys:
        info_dict[key] = []
    
    for one_info in info:
        language, role, career, food, score = one_info.split()
        info_dict[f'{language}|{role}|{career}|{food}'].append(int(score))
        
    for key in info_dict:
        info_dict[key].sort()
    
    answer = []
    for one_query in query:
        language, role, career, food, score = [data if data != '-' else None for data in one_query.split() if data != 'and']
        count = 0
        keys = make_keys(language, role, career, food)
        for key in keys:
            count += len(info_dict[key]) - bisect_left(info_dict[key], int(score))
        answer.append(count)
    
    return answer