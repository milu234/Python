#Python program to shuffle deck of cards
import itertools , random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

random.shuffle(deck)


n=int(input("Enter the no. of cards: "))
print("You Got : ")
for i in range(n):
    print(deck[i][0],"of" ,deck[i][1])
