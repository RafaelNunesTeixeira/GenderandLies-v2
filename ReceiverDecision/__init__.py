from otree.api import *
import csv
import random






c = Currency  # old name for currency; you can delete this.

doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'rectask'
    duration = 10
    fee = 1.00
    bonus = 4.00
    players_per_group = None
    num_rounds = 11
    instructions_template = 'Dictator/instructions.html'
    # """Amount allocated to each player"""
    rounds = 15
    contact = 'Dictator/contact.html'
    papercups_template = 'Dictator/papercups.html'
    timeout = 5
    role= 'Participant 2'
    cases = [
        [1, "Unites States", "Male", "20-30", 2],
        [2, "Unites States", "Female", "20-30", 2],
        [3, "Unites States", "Male", "30-40", 2],
        [4, "Unites States", "Female", "30-40", 2],
        [5, "United Kingdom", "Male", "20-30", 2],
        [6, "United Kingdom", "Female", "20-30", 2],
        [7, "United Kingdom", "Male", "30-40", 2],
        [8, "United Kingdom", "Female", "30-40", 2],
        [9, "United Kingdom", "Male", "20-30", 1],
        [10, "United Kingdom", "Female", "20-30", 1],
        [11, "Unites States", "Male", "30-40", 1],
        [12, "Unites States", "Female", "30-40", 1],
        [13, "Netherlands", "Male", "20-30", 1],
        [14, "Netherlands", "Male", "30-40", 2],
        [15, "Netherlands", "Female", "30-40", 2],

    ]


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.seed = random.random()

    for player in subsession.get_players():
        random.seed(player.participant.seed)
        l1 = random.sample([1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10 , 11, 12,13,14,15], 15)
        teste=(player.round_number)-1
        case=l1[teste]-1
        player.case = Constants.cases[case][0]
        player.place = Constants.cases[case][1]
        player.gender =  Constants.cases[case][2]
        player.age =  Constants.cases[case][3]
        player.signal =  Constants.cases[case][4]



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    case=models.IntegerField()
    place = models.StringField()
    gender = models.StringField()
    age=models.StringField()
    signal=models.IntegerField()
    decision = models.IntegerField(
        choices=[[0, 'Keep'], [1, 'Punish']],
        widget=widgets.RadioSelect,)





class decision(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class decision1(Page):
    form_model = 'player'
    form_fields = ['decision']
    @staticmethod
    def vars_for_template(player: Player):
        place = player.place
        gender = player.gender
        age = player.age
        signal = player.signal
        round = player.round_number
        return dict(place=place, gender=gender, age=age, signal=signal, round=round)







page_sequence = [decision, decision1]
