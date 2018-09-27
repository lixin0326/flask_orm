from flask import Flask
from apps import create_app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

manage = Manager(app=create_app())

manage.add_command('run', Server(host='127.0.0.1', port=8080, threaded=True))

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
