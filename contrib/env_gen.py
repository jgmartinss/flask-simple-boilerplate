#!/usr/bin/env python

import sys
import uuid

CONFIG_STRING = """
ENV={}
DEBUG=True
SECRET_KEY={}
HOST=127.0.0.1
PORT=8000
DATABASE_PATH='sqlite:///db.sqlite3'
""".strip().format(
    sys.argv[1], uuid.uuid4().hex
)

# Writing our configuration file to '.env'
with open(".env", "w") as configfile:
	configfile.write(CONFIG_STRING)