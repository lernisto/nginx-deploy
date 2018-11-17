#!/usr/bin/env python3

import os
import venv

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ENV_DIR= os.path.join(PROJECT_DIR,"venv")
ENVPROMPT= os.path.basename(PROJECT_DIR)

venv.create(ENV_DIR,with_pip=True,prompt=ENVPROMPT)

bindir = os.path.join(ENV_DIR,'bin')
if os.path.isdir(bindir):
    print("source {}/activate".format(bindir))
else:
    print("{}/Scripts/activate.bat".format(ENV_DIR))

requirements = os.path.join(PROJECT_DIR,"src/requirements.txt")
print('pip install --upgrade pip')
print('pip install -r {}'.format(requirements))
