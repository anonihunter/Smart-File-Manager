import json
from pathlib import Path

# ---------- Default Configuration ----------

DEFAULT_CONFIG = {
    "default_directory": "C:/Python Projects/Files",

    "extension_mapping": {
        ".pdf": "Docs",
        ".txt": "Docs",
        ".docx": "Docs",

        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".bmp": "Images",

        ".mp4": "Videos",
        ".mkv": "Videos",

        ".mp3": "Audio",
        ".m4a": "Audio",

        ".zip": "Zip File"
    },

    "duplicates": {
        "mode": "move"
    },

    "logging": {
        "enabled": True,
        "level": "INFO",
        "filename": "smart_file_manager.log"
    },

    "monitoring": {
        "recursive": True
    },

    "statistics": {
        "enabled": True
    }
}

CONFIG_FILE = Path("config.json")


def load_config():
    """
    Loads configuration from config.json.
    If anything goes wrong, default configuration is used.
    """

    if not CONFIG_FILE.exists():
        print("config.json not found. Using default configuration.")
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r") as file:
            user_config = json.load(file)

        config = DEFAULT_CONFIG.copy()

        for key, value in user_config.items():
            if isinstance(value, dict) and key in config:
                config[key].update(value)
            else:
                config[key] = value

        return config

    except json.JSONDecodeError:
        print("Invalid config.json. Using default configuration.")
        return DEFAULT_CONFIG

    except Exception as e:
        print(f"Configuration Error: {e}")
        return DEFAULT_CONFIG


config = load_config()