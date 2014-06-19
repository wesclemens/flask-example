import os
import glob
import importlib

endpoint_dir = os.path.dirname(__file__)
for path in glob.iglob(os.path.join(endpoint_dir, "*.py")):
    module = os.path.basename(path)[:-3]
    if module != '__init__':
        importlib.import_module('.' + module, __name__)
