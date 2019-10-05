
from .phases.beginning_phase import *
from .phases.main_phase import *
from .phases.combat_phase import *
from .phases.ending_phase import *


class Turn:

    def __init__(self):

        self.no = 1
        self.phases = {

            'Beginning Phase': {
                'Untap Step': step_untap,
                'Upkeep Step': step_upkeep,
                'Draw Step': step_draw
            },


            'First Main Phase': {
                'Main Step': step_main
            },


            'Combat Phase': {
                'Beginning of Combat Step': step_beginning_of_combat,
                'Declare Attackers Step': step_declare_attackers,
                'Declare Blockers Step': step_declare_blockers,
                'Combat Damage Step': step_combat_damage,
                'End of Combat Step': step_end_of_combat
            },


            'Second Main Phase': {
                'Main Step': step_main
            },


            'Ending Phase': {
                'End Step': step_end,
                'Cleanup Step': step_cleanup
            }

        }

        # self.phases = [
        #     'Beginning Phase',
        #     'First Main Phase',
        #     'Combat Phase',
        #     'Second Main Phase',
        #     'Ending Phase'
        # ]
        # for phase in self.phases:
        #     print(id(phase))

    def make_turn(self, players, owner):
        print(f'{owner} starts their turn!')

        for phase_name, step_dict in self.phases.items():
            print(f"It's {owner}'s {phase_name}")
            # if not step_dict(players, owner):
            if not self.prokladka(step_dict, players, owner):
                return False
        return True


    @staticmethod
    def prokladka(step_dict, players, owner):

        # print(step_dict)
        # input('click')


        for key, value in step_dict.items():
            if not key == 'Main Step':
                print(f"It's {owner}'s {key}")
            if not value(players, owner):
                return False
        return True

