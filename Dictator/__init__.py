from otree.api import *



c = Currency  # old name for currency; you can delete this.

doc = """
experiment
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    duration = 4
    fee = 0.35
    bonus = 4.00
    players_per_group = None
    num_rounds = 1
    instructions_template = __name__ +'/instructions.html'
    # """Amount allocated to each player"""
    rounds = 1
    contact = __name__ +'/contact.html'
    papercups_template = __name__ + '/papercups.html'
    timeout = 5
    role= 'Participant 1'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    ##demographics
    gender = models.IntegerField(
        label='What is your gender?',
        choices=[[1, 'Male'], [2, 'Female'], [3, 'Other']],
        widget=widgets.RadioSelect,
    )

    age = models.IntegerField(label='How old are you?')

    residence = models.IntegerField(
        label='Place of birth?',
        choices=[[1, 'UK'], [2, 'U.S.'], [3, 'The Netherlands'], [4, 'Belgium'],[5, 'France'],[6, 'Germany'],[7, 'Other']],
        widget=widgets.RadioSelect,
    )
    siblings = models.IntegerField(
        label='Do you have siblings?',
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelect,
    )


    ##check-up

    q1 = models.IntegerField(
        choices=[[1, '10%'], [2, '20%'],[3, '50%'],[4,'80%']],
        widget=widgets.RadioSelect,
    )

    q2 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelect,
    )

    q3 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelect,
    )

    q4 = models.IntegerField(
        choices=[2, 4, 1, 8, 100, 200],
        widget=widgets.RadioSelect,
    )

    q5 = models.IntegerField(
        choices=[33, 888, 10, 100, 88, 8],
        widget=widgets.RadioSelect,
    )
    q6 = models.IntegerField(
        choices=[200, 400, 500, 600, 800],
        widget=widgets.RadioSelect,
    )
    q7 = models.IntegerField(
        choices=[200, 400, 500, 600, 800],
        widget=widgets.RadioSelect,
    )
    q8 = models.IntegerField(
        choices=[[1, 'No. Participant 2 only knows the color informed by Participant 1.'], [2, 'Yes. Participant 2 knows the color that was randomly picked by the computer and received by Participants 1.']],
        widget=widgets.RadioSelect,
    )
    q9 = models.IntegerField(
        choices=[[1, 'Participant 1 loses 100 points, and Participant 2 loses 50 points.'],[2, 'Participant 1 loses 300 points, and Participant 2 loses 50 points.'],[3, 'Participant 1 loses 100 points, and Participant 2 loses 100 points.'],[4, 'Participant 1 loses 300 points, and Participant 2 loses 100 points.'],],
        widget=widgets.RadioSelect,
    )
    q10 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelect,
    )
    q11 = models.IntegerField(
        choices=[[1, 'Participant 1'], [2, 'Participant 2']],
        widget=widgets.RadioSelect,
    )


# FUNCTIONS



class Introduction(Page):
   pass


class demographics(Page):
   form_model='player'
   form_fields = ['age','gender','residence','siblings']




class questions(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11']

    def error_message(self, values):
        if int(values['q1']) != 2:
            return 'Question 1 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q2']) != 2:
            return 'Question 2 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q3']) != 1:
            return 'Question 3 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q4']) != 1:
            return 'Question 4 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q6']) != 600:
            return 'Question 6 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q7']) != 200:
            return 'Question 7 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q8']) != 1:
            return 'Question 8 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q9']) != 2:
            return 'Question 9 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q10']) != 2:
            return 'Question 10 is wrong. Please, read again the instructions below and give the correct answer.'
        if int(values['q11']) != 1:
            return 'Question 11 is wrong. Please, read again the instructions below and give the correct answer.'

class formation(Page):
    pass


class start(Page):
    pass



page_sequence = [start,demographics,formation,Introduction,questions]
