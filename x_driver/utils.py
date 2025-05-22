from pathlib import Path
import os
import json


def validate_playwright():
    return


def validate_activation():
    return

        
def load_json():
    pass


def load_config():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DRIVER_CONFIG_PATH = "bundles/driver/config.json"

    FULL_PATH = os.path.join(BASE_DIR, DRIVER_CONFIG_PATH)
    with open(FULL_PATH) as file:
        config = json.load(file)
        return config


def get_playwright_path():
    import playwright
    return Path(playwright.__file__).parent
