from pathlib import Path
import os
import json
from importlib.metadata import version


def validate_playwright():
    try:
        import playwright  # noqa

    except ImportError:
        return False, "Playwright not installed"

    supported_versions = ["1.52.0"]
    playwright_version = version("playwright")
    if playwright_version not in supported_versions:
        return False, (
            "Playwright version not compatibile with XDriver, "
            f"Current version {playwright_version}, "
            f"Recommended versions - {supported_versions}"
        )

    return True, ""


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
