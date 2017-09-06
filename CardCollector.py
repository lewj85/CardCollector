'''
CardCollector - by Jesse Lew
Python script to solve the "Coupon Collector's Problem" of probability theory
for a deck of 52 cards using Monte Carlo simulations.
'''

import random
import numpy as np
import matplotlib.pyplot as plt

# initialize variables
cards = 52
Trials = []

# get num of simulations from user
simulations = int(input('How many simulations would you like to run? '))


# collect cards, append result to Trials
def collect(cards):
    # reset values each trial
    loops = 0
    Deck = []

    while len(Deck) < cards:
        card = random.randint(1, cards)
        if card not in Deck:
            Deck.append(card)
        loops += 1

    return loops

# run simulations
for x in range(simulations):
    Trials.append(collect(cards))

# display results
print('Average:', np.average(Trials))
print('Median', np.median(Trials))
print('Minimum:', min(Trials))
print('Maximum:', max(Trials))
plt.hist(Trials, 100)   # 100 bins
plt.xlabel('Card selections')
plt.ylabel('Number of trials')
plt.show()
