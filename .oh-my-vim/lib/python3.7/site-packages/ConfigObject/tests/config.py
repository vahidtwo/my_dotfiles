# -*- coding: utf-8 -*-
from ConfigObject import config_module
import os
filename = os.path.join(os.path.dirname(__file__), 'config.ini')
config = config_module(__name__, __file__, filename)

