from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'
print(ENV)
print(ENV)
print(ENV)
print(ENV)
base_settings = [
    'components/common.py',  # standard django settings,  # postgres

    # Select the right env:
    'environments/{0}.py'.format(ENV),
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)