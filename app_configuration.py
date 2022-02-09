import os


class AppConfiguration:
    def __init__(self, app):
        self._app = app
        self.add_configurations()

    @property
    def app(self):
        return self._app

    def add_configurations(self) -> None:
        self.app.config.update(SECRET_KEY=os.environ.get('APP_SECRET_KEY'),
                               WTF_CSRF_SECRET_KEY=os.environ.get('SECRET_KEY_CSRF'),
                               ADMIN=os.environ.get('ADMIN_NAME'))
