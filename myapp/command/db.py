from __future__ import print_function, absolute_import
import os
import re
import sys

from flask.ext.script import prompt_bool, Manager

from .. import app, db

from .. import model

db_sub_manager = Manager(usage="Databases commands")

@db_sub_manager.command
def create_all():
    db.create_all()

@db_sub_manager.command
def drop_all():
    if prompt_bool(
            "This will cause loss of all data. Do you want to continue?"):
        db.drop_all()

@db_sub_manager.command
def shell():
    db_engine = app.config['SQLALCHEMY_DATABASE_URI'].split(':')[0]
    if db_engine in ('postgres', 'postgresql+psycopg2', 'postgresql'):
        _postgres_shell()

    elif db_engine == 'sqlite':
        _sqlite_shell()

    elif db_engine in ('mysql', 'mysql+mysqldb',
            'mysql+oursql', 'mysql+pymysql', 'mysql+mysqlconnector',
            'mysql+cymysql', 'mysql+zxjdbc',):
        _mysql_shell()

    else:
        print("Unknown database engine `%s`" % db_engine, file=sys.stderr)
        return 1

def _postgres_shell():
    args = ['psql',]
    env = os.environ
    conn_pat = re.compile(
            r'//((\w+)(:([^@]+))?@)?([\w\-\.]+)(:(\d+)?)?/(\w+)')
    match = conn_pat.search(app.config['SQLALCHEMY_DATABASE_URI'])
    if match.group(2):
        args.append('--username')
        args.append(match.group(2))
    if match.group(4):
        env['PGPASSWORD'] = match.group(4)
    if match.group(7):
        args.append('--port')
        args.append(match.group(7))
    args.append('--host')
    args.append(match.group(5))
    args.append('--dbname')
    args.append(match.group(8))
    os.execvpe('psql', args, env)

def _sqlite_shell():
    if app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite://':
        print("Cannot start shell for in-memery database.")
        return 1
    else:
        args = ['sqlite3', app.config['SQLALCHEMY_DATABASE_URI'][10:],]
        os.execvpe('sqlite3', args, os.environ)

def _mysql_shell():
    args = ['mysql']
    conn_pat = re.compile(
            r'//((\w+)(:([^@]+))?@)?([\w\-\.]+)(:(\d+)?)?/(\w+)')
    match = conn_pat.search(app.config['SQLALCHEMY_DATABASE_URI'])
    groups = match.groups()
    print(groups)
    if match.group(2):
        args.append('--user=%s' % match.group(2))
    if match.group(4):
        args.append('--password=%s' % match.group(4))
    if match.group(7):
        args.append('--port=%s' % match.group(7))
    args.append('--host=%s' % match.group(5))
    args.append('--database=%s' % match.group(8))
    os.execvpe('mysql', args, os.environ)

