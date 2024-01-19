# Bet simulations in blaze

### this algorithm actually proves that is impossible to win the roulette in blaze

# the rules

- there is 14 numbers
- the number has 3 possible colors
- white, red, black
- the roulette should be something like that

* ` ROULLET = [
'white', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red',
'black', 'red', 'black', 'red', 'black', 'red'
]`
* the prize is based on the colors, white has x14 of yout bet, red and black has x2
* you can bet any color, how many times you want, the min bet is 0.10

# Simulations

the simulations try to maximize the profit and optimize the loss, by beating only the profit when wining, and betting the amount of loss...

but that enormous amount of simulations and strategies like martingale vs fibonacci and kelly criterion, resulting and loss thouth the time.

you can modify, and try new parameters, such as gold, initial balance, inital_bet_amount, to see any diferences.

### also it`s impossible to predict the next color or the next number, the randomness of the nature, is amazing, and no pattern will provide an clue.

For example, if in a series of coin tosses the sequence "heads-tails-heads-tails" occurs, the gambler's fallacy would be to think that, based on these results, the next toss is more likely to be "heads." However, in a truly random process, each toss is independent and is not influenced by previous outcomes.
