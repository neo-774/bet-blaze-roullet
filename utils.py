
import random
from constants import ROULETTE, COLORS
random.shuffle(ROULETTE)

def generate_strategy(history):
    strategies = ["default", "martingale", "fibonacci"]
    best_strategy = None
    best_balance = float('-inf') 

    for strategy in strategies:
        final_balance = simulate_strategy(history, strategy)
        if final_balance > best_balance:
            best_balance = final_balance
            best_strategy = strategy

    return best_strategy

def simulate_strategy(history, strategy):
    base_bet_amount = 1
    current_balance = history[0]["initial_balance"]

    for bet in history:
        next_bet_amount = generate_next_bet_amount(bet, base_bet_amount, strategy)
        current_balance = generate_new_balance(current_balance, next_bet_amount, bet['roulette_result']['award'])

    return current_balance

 

def default_strategy(bet, diff):
    if bet['roulette_result']['current_balance'] > bet['initial_balance']:
        bet_amount = bet['roulette_result']['current_balance'] - bet['initial_balance']
        return round(bet_amount, 2)

    if diff < 0:
        bet_amount = min(diff / 2, bet['roulette_result']['current_balance'] / 1.5)
        if bet_amount < 0.10:
            return 0.10
        return bet_amount

    return 1


def martingale_strategy(bet, base_bet_amount):
    if not bet['roulette_result']['result']:
        return 2 * base_bet_amount
    else:
        return base_bet_amount


def fibonacci_strategy(bet, base_bet_amount): 
    if not bet['roulette_result']['result']:
        fib_sequence = [0, 1]
        while fib_sequence[-1] + fib_sequence[-2] <= base_bet_amount:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    else:
        return base_bet_amount



def generate_next_bet_amount(bet):
    diff = bet['initial_balance'] - bet['roulette_result']['current_balance'] 
    if diff >= 0:
        bet_amount = min(diff / 2, bet['roulette_result']['current_balance'] / 1.5)
        if bet_amount < 0.10:
            return 0.20
        return bet_amount
    else:
      return((abs(diff)+0.10)) 
       

def generate_award(
    balance,
    bet_color_index, 
    roulette_index_result,
    bet_amount,
  ):
    award = 0
    if bet_color_index == 0:
        award = bet_amount * 14
    if bet_color_index == 1 or bet_color_index == 2:
        award = bet_amount * 2
        
    old_balance_minus_bet = (round(balance, 2) - bet_amount)
    if bet_color_index == roulette_index_result: 
      current_balance = round(old_balance_minus_bet, 2) + award
      return {
         'old_balance': round(old_balance_minus_bet, 2),
         'current_balance': round(current_balance, 2), 
         'award': award,
         'bet_amount': bet_amount, 
         'result': True
        } 

    return {
       'old_balance': balance,
       'current_balance': old_balance_minus_bet, 
       'award': 0, 
       'bet_amount': bet_amount, 
       'result': False
       } 
    

    
def generate_new_balance(balance, bet_amount, award):
   return (balance-bet_amount) + award

def roulette_bet_number():
  return random.randrange(0, 14)

def generate_bet_number():
  return random.randrange(0, 14)
