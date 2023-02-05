from typing import List, NewType, Tuple

AttackLevel = NewType('AttackLevel', int)
StrengthLevel = NewType('StrengthLevel', int)
Experience = NewType('Experience', int)

'''
For every level, what is the minimum amount of experience needed

Example: Total exp needed for level 1 is TOTAL_EXP_NEEDED_AT_LEVEL[1]. Total exp needed for lvl 3 is TOTAL_EXP_NEEDED_AT_LEVEL[3]
'''
TOTAL_EXP_NEEDED_AT_LEVEL: List[Experience] = [0, 83, 174, 275, 386, 509, 645, 795, 960, 1143, 1345, 1568, 1814, 2086, 2386,
                                               2717, 3083, 3487, 3933, 4426, 4970, 5571, 6234, 6967, 7776, 8669, 9655, 10744,
                                               11946, 13273, 14739, 16357, 18144, 20117, 22295, 24700, 27355, 30287, 33524,
                                               37098, 41044, 45401, 50212, 55523, 61387, 67862, 75011, 82904, 91619, 101241,
                                               111864, 123593, 136543, 150841, 166628, 184058, 203302, 224549, 248008, 273909,
                                               302506, 334080, 368940, 407429, 449924, 496843, 548646, 605841, 668989, 738710,
                                               815689, 900680, 994518, 1098124, 1212514, 1338811, 1478254, 1632212, 1802195,
                                               1989872, 2197084, 2425865, 2678460, 2957347, 3265264, 3605231, 3980586, 4395011,
                                               4852573, 5357763, 5915538, 6531372, 7211307, 7962017, 8790868, 9705993, 10716374,
                                               11831925, 13063593, 14423464]

def generateWorkNeededPerLevel(levels: int) -> List[Experience]:
    '''
    Creates a list, such as TOTAL_EXP_NEEDED_AT_LEVEL, that describes the minimum exp needed per level
    '''
    # Roughly, we want to double every 7 levels
    initial_work: Experience = 83
    growth_factor: float = 1.10408951367

    # First, find the work we need to do from each level to the next
    work_per_level: List[Experience] = [initial_work]
    for i in range(0, levels - 1):
        last_experience_value = work_per_level[-1]
        exp_for_next_level = last_experience_value * growth_factor

        work_per_level.append(exp_for_next_level)

    # The total work should just be a running sum up to that level
    work_total_per_level: List[Experience] = [0, work_per_level[0]]
    for i in range(0, levels - 1):
        # Mathemtically equivalent to a running sum
        last_work_total_value = work_total_per_level[-1]
        exp_for_ith_level = int(last_work_total_value + work_per_level[i+1])

        work_total_per_level.append(exp_for_ith_level)

    return work_total_per_level
