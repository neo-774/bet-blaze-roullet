from constants import COLORS, ROULLET 
import matplotlib.pyplot as plt
from utils import generate_next_bet_amount, generate_award, generate_bet_number, roullet_bet_number


def roullet_run(num_sim, balance, bet_amount, bets, initial_balance):
    roullet_index_result = COLORS.index(ROULLET[roullet_bet_number()])
    bet_color = ROULLET[generate_bet_number()]
    bet_color_index = COLORS.index(bet_color)
    last_bet_amount = bet_amount
    bet_amount = 0.1
    if num_sim > 0:
        bet_amount = generate_next_bet_amount(bets[num_sim-1])

    roullet_result = generate_award(
        balance,
        bet_color_index,
        roullet_index_result,
        bet_amount,
    )
    bets.append({
        'bet_color': bet_color,
        'roullet_color': ROULLET[roullet_index_result],
        'initial_balance': initial_balance,
        'last_bet_amount': last_bet_amount,
        'num_sim': num_sim,
        'current_bet_amount': round(bet_amount, 2),
        'roullet_result': roullet_result
    })

    return bets


def loop_game():
    num_simulations = 1000
    initial_balance = 10
    balance = initial_balance
    goal = 15
    bets = []
    bet_amount = 3.5
    balances = []
    bet_amounts = [] 
     
    for num_sim in range(num_simulations):
        if num_sim == 0:
            bets = roullet_run(num_sim, balance, bet_amount, bets, initial_balance)
        else:
            current_balance = bets[num_sim - 1]['roullet_result']['current_balance']
            bets = roullet_run(num_sim, current_balance, bet_amount, bets, initial_balance)

        if bets and num_sim < len(bets):
            current_balance = bets[num_sim - 1]['roullet_result']['current_balance']
            balances.append(current_balance)
            bet_amounts.append(bets[num_sim - 1]['current_bet_amount'])

            if current_balance >= goal:
                print(f"Goal reached at simulation {num_sim}. Final balance: {current_balance}")
                break

            if current_balance < 0.10:
                print(f"Balance dropped below 1 at simulation {num_sim}. Final balance: {current_balance}")
                break

    return bets, balances, bet_amounts



def loops(): 
  num_loops = 100
  for loop in range(num_loops):
    result, balances, bet_amounts = loop_game() 

    plt.plot(range(len(balances)), balances, label='Balance')
    plt.plot(range(len(bet_amounts)), bet_amounts, label='Bet Amount', linestyle='dashed')
    plt.xlabel('Simulation Iteration')
    plt.ylabel('Value')
    plt.title('Roulette Simulation')
    plt.legend()
    plt.show()

loops()