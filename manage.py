import os
from flask.ext.script import Manager, Shell
from app import create_app, db
from flask.ext.migrate import Migrate, MigrateCommand
from app.models import User, Role, Task, Category

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Task=Task, Category=Category)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

	

if __name__ == '__main__':
	manager.run()