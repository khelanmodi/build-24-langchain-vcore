from backend.app import create_app
from backend.config import AppConfig

app_config = AppConfig()
app = create_app(app_config=app_config)
