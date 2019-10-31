"""
Chooses which settings should be imported depending on existence of environment
variable.
"""
from .mode import MODE


if MODE == 'DEV':
    from .development import *
else:
    from .production import *
