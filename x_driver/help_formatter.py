import argparse

helper_art = """
 __   _______       _                
 \ \ / /  __ \     (_)               
  \ V /| |  | |_ __ ___   _____ _ __ 
   > < | |  | | '__| \ \ / / _ \ '__|
  / . \| |__| | |  | |\ V /  __/ |   
 /_/ \_\_____/|_|  |_| \_/ \___|_|   v0.0.1(beta)

 Make your playwright undetectable for web scraping

 Usage:
    x_driver <command> [options]

 Commands:
    status         :    Check the status of XDriver Session
    activate       :    Activate the XDriver Session
    deactivate     :    Deactivate the XDriver Session

Options:
    --force        :    Force activation (override checks)
"""


class HelpFormatter(argparse.RawTextHelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            default = self._get_default_metavar_for_optional(action)
            return default
        else:
            return ", ".join(action.option_strings)

    def _split_lines(self, text, width):
        return super()._split_lines(text, width)
