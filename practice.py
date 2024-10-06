import random


HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN VALUES)


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        result = flip_coin()
        if result == HEADS:
            current_funds += current_bet
            current_bet = min_bet
        else:
            current_funds -= #here
            current_bet *= 2
            steps_to_lose += 1
        if current_bet > max_bet:
            current_bet = max_bet
        return steps_to_lose
                        
                        

if__name__ == "__main__":
    starting_funds = 100
    min_bet = 1
    max_bet = 100
    steps_to_loose = play_martingale(starting_funds=starting_funds, min_bet=min_bet, max_bet=max_bet)
    print(f"Steps to Lose: {steps_to_loose}")
    if steps_to_loose < 800:
        print("You won!")
    else:       
        print("You Lost!")
    
        