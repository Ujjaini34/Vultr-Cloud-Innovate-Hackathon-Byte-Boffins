import os
from app import app  # Replace 'app' with the name of your main file (without .py)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 3000)))
