"""App entry point."""
from flask_pytorch_web_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
