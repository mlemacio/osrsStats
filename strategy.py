from constants import *
from enum import Enum
import random

'''
All the available strategies for the user to choose from. Should match 1:1 with all available strategy functions
'''


class Strategy(Enum):
    ATTACK_FIRST = 1
    STRENGTH_FIRST = 2
    BALANCED = 3
    ATTACK_FIVE = 4
    RANDOM = 5
    CONTROLLED = 6
    CUSTOM = 7


def obvious_check(attack_level: AttackLevel,
                  strength_level: StrengthLevel) -> Tuple[float, float]:
    ''' 
    Eliminates the need to check edge cases in the actual strategy
    '''
    if(attack_level == 99 and strength_level == 99):
        raise ValueError(
            "Both Attack and Strength are maxed... why are you still going?")

    # Attack is maxed, everything funnels into strength
    if(attack_level == 99):
        return (0, 1)

    # Like-wise with strength
    if(strength_level == 99):
        return (1, 0)

    return None


def attack_first_strategy(attack_level: AttackLevel,
                          strength_level: StrengthLevel) -> Tuple[float, float]:
    return (1, 0)


def strength_first_strategy(attack_level: AttackLevel,
                            strength_level: StrengthLevel) -> Tuple[float, float]:
    return (0, 1)


def balanced_strategy(attack_level: AttackLevel,
                      strength_level: StrengthLevel) -> Tuple[float, float]:
    return (.5, .5)


def attack_five_strategy(attack_level: AttackLevel,
                         strength_level: StrengthLevel) -> Tuple[float, float]:
    # If our attack is within 5 levels of out strength, focus on that
    strategy_to_use = strength_first_strategy
    if(attack_level < strength_level + 5):
        strategy_to_use = attack_first_strategy

    return strategy_to_use(attack_level, strength_level)


def random_strategy(attack_level: AttackLevel,
                    strength_level: StrengthLevel) -> Tuple[float, float]:

    val = random.random()
    return (val, 1 - val)


def controlled_strategy(attack_level: AttackLevel,
                        strength_level: StrengthLevel) -> Tuple[float, float]:
    # In theory, the last .34 should go into defense
    return (.33, .33)


def custom_strategy(attack_level: AttackLevel,
                    strength_level: StrengthLevel) -> Tuple[float, float]:
    if(strength_level < 90):
        return balanced_strategy(attack_level, strength_level)

    return attack_first_strategy(attack_level, strength_level)
