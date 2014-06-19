"""
This module contains all the command line entry points.
"""
from __future__ import absolute_import

from flask.ext.script import Manager

from .. import app

manager = Manager(app)

from .db import db_sub_manager
manager.add_command('database', db_sub_manager)

from .cache import cache_sub_manager
manager.add_command('cache', cache_sub_manager)

@manager.shell
def make_shell_context():
    from .. import db, cache
    from .. import model
    return dict(app=app, db=db, model=model, cache=cache)

def main_cli():
    """
    This is the main CLI entry point.
    """
    manager.run()

