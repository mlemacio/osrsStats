from bisect import *
from random import randint
from constants import *
from strategy import *


def chanceToHit(attack_level: AttackLevel) -> float:
    '''
    Returns the chance to hit based on a given attack level. Currently linear
    '''
    return (attack_level / 100)


def maxHit(strength_level: StrengthLevel) -> Experience:
    '''
    Returns the maximum hit available to a user at this strength level
    '''
    return strength_level


def damageDone(attack_level: AttackLevel, strength_level: StrengthLevel) -> Experience:
    '''
    On any given attack, what is the damage done to the enemy
    '''
    # The attack first needs to hit
    chance = chanceToHit(attack_level) * 100
    attack_needed_to_hit = randint(1, 100)

    did_hit = (chance >= attack_needed_to_hit)

    if(did_hit == False):
        return 0

    # And then we can see how much damage we did
    return randint(1, maxHit(strength_level))


def calcExpFromDamage(damage: int):
    '''
    Returns how much exp one gains from a given amount of damage
    '''
    return damage


def getLevelFromExpTotal(exp: Experience):
    '''
    Returns what level the user is at for a given category based on their total experience
    '''
    if(exp < 0):
        raise ValueError("Experience value is less than zero")

    # This is just a built-in way of doing a binary search on a sorted list
    # We want to find where our input exp would land us in the list and return the index to the left
    return bisect_right(TOTAL_EXP_NEEDED_AT_LEVEL, exp) - 1


def getStrategyFunc(strategy: Strategy):
    '''
    Grabs the corresponding strategy function based on what strategy a user passed in  
    '''
    strategy_to_func = {
        Strategy.ATTACK_FIRST: attack_first_strategy,
        Strategy.STRENGTH_FIRST: strength_first_strategy,
        Strategy.BALANCED: balanced_strategy,
        Strategy.ATTACK_FIVE: attack_five_strategy,
        Strategy.RANDOM: random_strategy,
        Strategy.CONTROLLED: controlled_strategy,
        Strategy.CUSTOM: custom_strategy,
    }

    if(strategy not in strategy_to_func):
        raise ValueError("Strategy \'" + strategy.name + "\' was not found")

    return strategy_to_func[strategy]


def run_strategy(strategy: Strategy):
    '''
    Simulates a strategy to get to both 99 attack and 99 strength
    '''
    strategy_func = getStrategyFunc(strategy)

    # Start the player at lvl 1 for both
    curr_attack_exp: Experience = 83
    curr_strength_exp: Experience = 83

    num_loops = 0

    while(True):
        # Calculate current attack level (this *probably* doesn't need to be done every cycle)
        attack_level: AttackLevel = getLevelFromExpTotal(curr_attack_exp)
        strength_level: StrengthLevel = getLevelFromExpTotal(curr_strength_exp)

        # At this point, there is no more training to do
        if(attack_level == 99 and strength_level == 99):
            print("Strategy " + strategy.name +
                  " takes " + str(num_loops) + " hits")
            return num_loops

        # Simulate a melee hit
        damage = damageDone(attack_level, strength_level)
        exp: Experience = calcExpFromDamage(damage)
        num_loops += 1

        # How much of our exp should go into what categry
        exp_attack_weight: float = 0.0
        exp_strength_weight: float = 0.0

        # Check if there's something obvious to do before we run it through a strategy
        obvious_val = obvious_check(attack_level, strength_level)
        if(obvious_val != None):
            exp_attack_weight, exp_strength_weight = obvious_val
        else:
            exp_attack_weight, exp_strength_weight = strategy_func(
                attack_level, strength_level)

        # Apply the weights and update our total exp
        curr_attack_exp += (exp_attack_weight * exp)
        curr_strength_exp += (exp_strength_weight * exp)
