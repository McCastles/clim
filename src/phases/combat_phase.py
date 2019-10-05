
# def start_combat_phase(players, owner):
#     steps = {

#         'Beginning of Combat Step' : step_beginning_of_combat,
#         'Declare Attackers Step'   : step_declare_attackers,
#         'Declare Blockers Step'    : step_declare_blockers,
#         'Combat Damage Step'       : step_combat_damage,
#         'End of Combat Step'       : step_end_of_combat
    
#     }
#     for key, value in steps:
#         print(f"It's {owner}'s {key}.")
#         if not value(players, owner):
#             return False
#     return True

def step_beginning_of_combat(players, owner):
    return True

def step_declare_attackers(players, owner):
    return True

def step_declare_blockers(players, owner):
    return True

def step_combat_damage(players, owner):
    return True

def step_end_of_combat(players, owner):
    return True
