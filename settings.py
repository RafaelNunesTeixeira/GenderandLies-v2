from os import environ

environ['OTREE_PRODUCTION'] = "1"

SESSION_CONFIGS = [
    dict(
        name='liesbloodylies',
        app_sequence=['Dictator', 'DictatorDecision','enddictator'],
        num_demo_participants=2,
    ),
    dict(
        name='liesbloodyliesintro',
        app_sequence=['Dictator'],
        num_demo_participants=2,
    ),
    dict(
        name='liesbloodyliespdecision',
        app_sequence=['DictatorDecision'],
        num_demo_participants=2,
    ),
    dict(
        name='enddictator',
        app_sequence=['enddictator'],
        num_demo_participants=2,
    ),

    dict(
        name='topunishornottopunish',
        app_sequence=['Receiver','ReceiverDecision','Beliefs','endreceiver'],
        num_demo_participants=2,
    ),

    dict(
        name='topunishornottopunishintro',
        app_sequence=['Receiver'],
        num_demo_participants=2,
    ),
    dict(
        name='topunishornottopunishdecision',
        app_sequence=['ReceiverDecision'],
        num_demo_participants=2,
    ),
    dict(
        name='Beliefs',
        app_sequence=['Beliefs'],
        num_demo_participants=2,
    ),
    dict(
        name='endreceiver',
        app_sequence=['endreceiver'],
        num_demo_participants=2,
    ),
    dict(
        name='survey',
        app_sequence=['survey'],
        num_demo_participants=2,
    ),
    dict(
        name='svo',
        app_sequence=['svo'],
        num_demo_participants=2,
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ROOMS = [
    dict(
        name='ExperimentG1',
        display_name='Experiment - ABS1',
    ),

    dict(
        name='ExperimentG2',
        display_name='Experiment - ABS2',
        participant_label_file='_rooms/ABS.txt',
    ),

    dict(
        name='ExperimentG3',
        display_name='Experiment - ABS3',
    ),
    dict(
        name='ExperimentG4',
        display_name='Experiment - ABS4',
        participant_label_file='_rooms/ABS.txt',
    ),
]

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')



ADMIN_USERNAME = 'bu'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'bu'


DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3844923960320'

INSTALLED_APPS = ['otree']



PARTICIPANT_FIELDS = ['seed']