card_val = {'2': 1,
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 0,
            '8': 0,
            '9': 0,
            '0': -1, # use '0' for 10 to keep everything a single character
            '`': -1,
        }
deck = {'2': 32,
        '3': 32,
        '4': 32,
        '5': 32,
        '6': 32,
        '7': 32,
        '8': 32,
        '9': 32,
        '0': 32*4, # use '0' for 10 to keep everything a single character
        '`': 32,
        }
cards = 416
def prob():
    print("Prob:")
    print("A: {:.1f}%|2: {:.1f}%|3: {:.1f}%|4: {:.1f}%|5: {:.1f}%|6: {:.1f}%|7: {:.1f}%|8: {:.1f}%|9: {:.1f}%|10: {:.1f}%|".format(((deck['`'])/cards)*100,100*(deck['2'])/cards,100*(deck['3'])/cards,100*(deck['4'])/cards,100*(deck['5'])/cards,100*(deck['6'])/cards,100*(deck['7'])/cards,100*(deck['8'])/cards,100*(deck['9'])/cards,100*(deck['0'])/cards))
count = 0
while (True):
    print("Count: {}".format(count))
    prob()
    try:
        user = str(input(">> ")).upper()  
        print(user)  
        deck[user] -=1
        cards-=1
        count = count + card_val[user]

    except KeyError:
        pass
        

    