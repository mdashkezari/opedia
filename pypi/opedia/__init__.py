
import os
import sys
sys.path.append(os.path.dirname(__file__))
import common as com
import warnings


class API:
    """ construct and configure an instance of the RESTful API """
    def __init__(self, api_key):
        self.api_key = api_key
        self.tokenPath = com.getTokenPath()
        com.saveToken(self.tokenPath, self.api_key)




if sys.version_info < (3, 0):
    warnings.warn(
        ('Python 2 is not supported anymore. '
         'Please transition to Python 3 to be able to receive updates and fixes.'),
        UserWarning
    )

__version__ = '0.2.75'
__all__ = []
