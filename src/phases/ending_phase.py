
# def start_ending_phase(players, owner):
#     steps = {

#         'End Step'     : end_untap,
#         'Cleanup Step' : cleanup_upkeep
    
#     }
#     for key, value in steps:
#         print(f"It's {owner}'s {key}.")
#         if not value(players, owner):
#             return False
#     return True

def step_end(players, owner):
    return True

def step_cleanup(players, owner):
    return True
