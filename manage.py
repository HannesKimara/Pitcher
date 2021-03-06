from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Comment, Pitch

app = create_app('production')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('serve',Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell():
    return dict(db = db, User = User, Comment = Comment, Pitch = Pitch, app=app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()