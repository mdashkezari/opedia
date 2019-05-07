
import sys
import warnings


if sys.version_info < (3, 0):
    warnings.warn(
        ('Python 2 is not supported anymore. '
         'Please transition to Python 3 to be able to receive updates and fixes.'),
        UserWarning
    )


__version__ = '0.2.55'

__all__ = []