import random
import math
married=[]
Girls = ["mona","sara","atie","nac","elnaz","maryam","narges","anali","marjan"]
Boys = ["ali","amir","mohammad","beny","foad","mahdi","farid","moeen","saeed"]
def search(married,boy,girl):
    for j in married:
        if j[0]==boy:
            return 1
        if j[1]==girl:
            return 1
    else:
        return 0
while True :
    g=random.choice(Boys)
    boy=str(g)
    b=random.choice(Girls)
    girl=str(b)
    n=search(married,boy,girl)
    if n==0:
        married.append((boy,girl))
        if len(married)==9:
            print(married)
            break