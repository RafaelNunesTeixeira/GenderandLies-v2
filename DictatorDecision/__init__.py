from otree.api import *
import random

c = Currency  # old name for currency; you can delete this.

doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'taskp1'
    players_per_group = 2
    num_rounds = 2
    instructions_template =  'Dictator/instructions.html'
    # """Amount allocated to each player"""
    rounds = 2
    contact =  'Dictator/contact.html'
    papercups_template = 'Dictator/papercups.html'
    role = 'Participant 1'

class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    for player in subsession.get_players():
        player.color= player.round_number


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    color = models.IntegerField()


    decision = models.IntegerField(
        choices=[[0, 'green'], [1, 'blue']],
        widget=widgets.RadioSelect,
    )


class decision1(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(player: Player):
        color=player.color
        return dict(color=color)

    @staticmethod
    def js_vars(player: Player):
        return dict(color=player.color)


page_sequence = [decision1]
