from x_driver.utils import validate_playwright, get_playwright_path, load_config
import os
import shutil


class ActivatorScript:

    def _patch(self):
        """
        Core patcher, backup the orginal file,
        and modify it with the patched files.
        """

        PLAYWRIGHT_PATH = get_playwright_path()
        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

        config = load_config()
        for filename, filepath in config.items():
            # Backup the orginal source file
            CURRENT_FILEPATH = os.path.join(PLAYWRIGHT_PATH, "driver", filepath, filename)
            BACKUP_FILEPATH = os.path.join(PLAYWRIGHT_PATH, "driver", filepath, f"xdriver_{filename}")
            os.rename(CURRENT_FILEPATH, BACKUP_FILEPATH)

            # Patching
            PATCH_FILEPATH = os.path.join(CURRENT_DIR, "bundles/driver", filename)
            shutil.copy(PATCH_FILEPATH, CURRENT_FILEPATH)

        # Patching root file
        INIT_FILEPATH = os.path.join(PLAYWRIGHT_PATH, "__init__.py")
        with open(INIT_FILEPATH, 'r') as file:
            original_contents = file.read()

        patched_init = (
            'print("Running inside the XDriver session")\n'
            + original_contents
        )
        with open(INIT_FILEPATH, 'w') as file:
            file.write(patched_init)

    def _unpatch(self):
        """
        Core unpatcher, delete the patched files
        and replace it with the backuped files.
        """
        pass

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
        patched = self.status()
        if patched:
            return True, "Already active"

        self._patch()
        patched = self.status()
        if not patched:
            return False, "Faled to activate"

        return True, "Activated"

    def deactivate(self):
        """
        Validate the patches and
        initiate the unpatching
        """

        # Checked status
        patched = self.status()
        if not patched:
            return False, "Not activated"

        self._unpatch()
        patched = self.status()
        if patched:
            return False, "Failed to deactivate"

        return True, "Deactivated"

    def status(self):
        pass
