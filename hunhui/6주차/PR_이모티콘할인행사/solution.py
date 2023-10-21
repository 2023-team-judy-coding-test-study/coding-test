from itertools import product

def solution(users, emoticons):
    rateList, caseList = list(product([10, 20, 30, 40], repeat = len(emoticons))), []

    for rates in rateList:
        emoPlus, emoPurchase = 0, 0
        for customerRate, customerPrice in users:
            priceList = [int(emoticons[i] * (100 - rates[i]) / 100) for i in range(len(rates))]
            purchase = []
            for rate in rates:
                if rate >= customerRate:
                    purchase.append(1)
                else:
                    purchase.append(0)
            cond = sum(purchase[i] * priceList[i] for i in range(len(priceList))) 
            if cond >= customerPrice:
                emoPlus += 1
            else:
                emoPurchase += cond
        caseList.append([emoPlus, emoPurchase])

    caseList.sort(key= lambda x : (x[0], x[1]), reverse=True)
    return caseList[0]