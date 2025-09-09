import os
import shutil

from x_driver.utils import (get_playwright_path, load_config,
                            validate_playwright)


class Activator:

    def _patch(self):
        """
        Core patcher, backup the orginal file,
        and modify it with the patched files.
        """
        PLAYWRIGHT_PATH = get_playwright_path()
        PACKAGE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "package")
        NODE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "node")
        BACKUP_PACKAGE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "package_1")
        BACKUP_NODE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "node_1")
        os.rename(PACKAGE_PATH, BACKUP_PACKAGE_PATH)
        # os.rename(NODE_PATH, BACKUP_NODE_PATH)

        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
        PATCH_PACKAGE = os.path.join(CURRENT_DIR, "bundles", "package")
        PATCH_NODE = os.path.join(CURRENT_DIR, "bundles", "node")
        shutil.copytree(PATCH_PACKAGE, PACKAGE_PATH)
        # shutil.copy2(PATCH_NODE, NODE_PATH)
        self._init_patcher(mode="patch")

    def _unpatch(self):
        """
        Core unpatcher, delete the patched files
        and replace it with the backuped files.
        """
        PLAYWRIGHT_PATH = get_playwright_path()
        PACKAGE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "package")
        NODE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "node")
        BACKUP_PACKAGE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "package_1")
        BACKUP_NODE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "node_1")

        shutil.rmtree(PACKAGE_PATH)
        # os.remove(NODE_PATH)

        os.rename(BACKUP_PACKAGE_PATH, PACKAGE_PATH)
        # os.rename(BACKUP_NODE_PATH, NODE_PATH)

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
        return True, "Activated"

    def deactivate(self):
        """
        Validate the patches and
        initiate the unpatching
        """

        # Checked status
        patched, status_text = self.status()
        if not patched:
            return False, "Not activated"

        self._unpatch()
        return True, "Deactivated"

    def status(self):
        PLAYWRIGHT_PATH = get_playwright_path()
        BACKUP_PACKAGE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "package_1")
        BACKUP_NODE_PATH = os.path.join(PLAYWRIGHT_PATH, "driver", "node_1")

        if os.path.exists(BACKUP_PACKAGE_PATH) or os.path.exists(BACKUP_NODE_PATH):
            return True, "Activated"
        return False, "Deactivated"

    def _init_patcher(self, mode):
        PLAYWRIGHT_PATH = get_playwright_path()
        INIT_FILEPATH = os.path.join(PLAYWRIGHT_PATH, "__init__.py")
        patch_line = 'print("\033[92m[-] XDriver INFO: Session Active\033[0m")\n'

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
