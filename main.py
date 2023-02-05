from play import run_strategy
from strategy import *

if __name__ == '__main__':
    run_strategy(Strategy.ATTACK_FIRST)
    run_strategy(Strategy.STRENGTH_FIRST)
    run_strategy(Strategy.BALANCED)
    run_strategy(Strategy.RANDOM)
    run_strategy(Strategy.CONTROLLED)
    run_strategy(Strategy.ATTACK_FIVE)
    run_strategy(Strategy.CUSTOM)