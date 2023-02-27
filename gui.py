from flaskwebgui import FlaskUI
from main import app


FlaskUI(server='flask', app= app, fullscreen=True, port=1234,).run()
