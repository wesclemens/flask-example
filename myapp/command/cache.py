from __future__ import print_function, absolute_import
import sys

from flask.ext.script import prompt_bool, Manager

from .. import app, cache

cache_sub_manager = Manager(usage="Cache commands")

@cache_sub_manager.command
def clear_all():
    warn_incompatible_type()
    cache.clear()

@cache_sub_manager.command
def get(key):
    warn_incompatible_type()
    print(cache.get(key))

@cache_sub_manager.command
def set(key, value, timeout):
    warn_incompatible_type()
    cache.set(key, value, int(timeout))

@cache_sub_manager.command
def delete(key):
    warn_incompatible_type()
    cache.delete(key)

def warn_incompatible_type():
    if app.config['CACHE_TYPE'] in ('null', 'simple'):
        print("WARNING: Cache type %s will not work as expected with commands"
                % app.config['CACHE_TYPE'], file=sys.stderr)
