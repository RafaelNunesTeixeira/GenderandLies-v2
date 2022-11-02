from otree.api import *


c = Currency  # old name for currency; you can delete this.

doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1
    contact = 'enddictator/contact.html'
    papercups_template = __name__ + '/papercups.html'

class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    pass



class Group(BaseGroup):
    pass

class Player(BasePlayer):
   exp=models.BooleanField(label="Have you ever participated in a similar experiment?")
   strategy = models.StringField(label="What motivated your decision?")


class end(Page):
    pass

class discussion(Page):
    form_model = 'player'
    form_fields = ['exp','strategy']


page_sequence = [discussion, end]
