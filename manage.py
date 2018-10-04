import click

from unittest import TestLoader, runner

from flask import current_app
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.auth import models


app = create_app(__name__, 'dev')
manager = Manager(app)

runserver = Server(host="127.0.0.1", port=8000)
manager.add_command("runserver", runserver)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=current_app, db=db, models=models)


@manager.command
def fake_user():
    db.drop_all(bind=None)
    db.create_all(bind=None)

    user = models.User(
        first_name=u'Test',
        last_name=u'Tests',
        username=u'tests',
        email=u"test@gmail.com",
        _password=u'123456'
    )
    db.session.add(user)
    db.session.commit()


@manager.command
def tests():
    loader = TestLoader()
    test = loader.discover('tests/')
    testrunner = runner.TextTestRunner(verbosity=2)
    testrunner.run(test)


if __name__ == '__main__':
    manager.run()
