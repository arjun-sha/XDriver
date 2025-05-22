import os
import shutil

from x_driver.utils import (get_playwright_path, load_config,
                            validate_playwright)


class ActivatorScript:

    def _patch(self):
        """
        Core patcher, backup the orginal file,
        and modify it with the patched files.
        """

        config = load_config()
        PLAYWRIGHT_PATH = get_playwright_path()
        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

        for filename, filepath in config.items():
            PATCH_FILEPATH = os.path.join(CURRENT_DIR, "bundles/driver", filename)
            CURRENT_FILEPATH = os.path.join(
                PLAYWRIGHT_PATH, "driver", filepath, filename
            )
            BACKUP_FILEPATH = os.path.join(
                PLAYWRIGHT_PATH, "driver", filepath, f"xdriver_{filename}"
            )

            os.rename(CURRENT_FILEPATH, BACKUP_FILEPATH)
            shutil.copy(PATCH_FILEPATH, CURRENT_FILEPATH)

        self._init_patcher(mode="patch")

    def _unpatch(self):
        """
        Core unpatcher, delete the patched files
        and replace it with the backuped files.
        """
        config = load_config()
        PLAYWRIGHT_PATH = get_playwright_path()

        for filename, filepath in config.items():
            CURRENT_FILEPATH = os.path.join(
                PLAYWRIGHT_PATH, "driver", filepath, filename
            )
            BACKUP_FILEPATH = os.path.join(
                PLAYWRIGHT_PATH, "driver", filepath, f"xdriver_{filename}"
            )
            if not os.path.exists(BACKUP_FILEPATH):
                continue

            os.remove(CURRENT_FILEPATH)
            os.rename(BACKUP_FILEPATH, CURRENT_FILEPATH)

        self._init_patcher(mode="unpatch")

    def activate(self, force: bool = False):
        """
        Validates the playwright versions
        and initiate the patches.
        """

        # Validating the playwright installaton
        valid, message = validate_playwright()
        if not valid and not force:
            return valid, message

        # Returning True if already patched.
        patched, status_text = self.status()
        if patched and status_text != "Corrupted":
            return True, "Already active"

        self._patch()
        patched, status_text = self.status()
        if not patched and status_text != "Corrupted":
            return False, "Faled to activate"

        return True, "Activated"

    def deactivate(self):
        """
        Validate the patches and
        initiate the unpatching
        """

        # Checked status
        patched, status_text = self.status()
        if not patched and status_text != "Corrupted":
            return False, "Not activated"

        self._unpatch()
        patched, status_text = self.status()
        if patched and status_text != "Corrupted":
            return False, "Failed to deactivate"

        return True, "Deactivated"

    def status(self):

        config = load_config()
        PLAYWRIGHT_PATH = get_playwright_path()

        all_status = []

        for filename, filepath in config.items():
            BACKUP_FILEPATH = os.path.join(
                PLAYWRIGHT_PATH, "driver", filepath, f"xdriver_{filename}"
            )
            if os.path.exists(BACKUP_FILEPATH):
                all_status.append(True)
                continue
            all_status.append(False)

        if all(all_status):
            return True, "Activated"

        if not any(all_status):
            return False, "Deactivated"

        return False, "Corrupted"

    def _init_patcher(self, mode):
        PLAYWRIGHT_PATH = get_playwright_path()
        INIT_FILEPATH = os.path.join(PLAYWRIGHT_PATH, "__init__.py")
        patch_line = 'print("Running inside the XDriver session")\n'

        # Reading init file
        with open(INIT_FILEPATH, "r") as file:
            original_contents = file.read()

        if mode == "patch":
            modifed_content = patch_line + original_contents
        else:
            modifed_content = original_contents.replace(patch_line, "")

        # Writing the init
        with open(INIT_FILEPATH, "w") as file:
            file.write(modifed_content)
