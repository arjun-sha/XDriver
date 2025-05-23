import argparse

from x_driver.activator_script import Activator
from x_driver.help_formatter import HelpFormatter, helper_art
from x_driver.logger import logger


def activator():
    parser = argparse.ArgumentParser(
        prog="x_driver", description=(helper_art), formatter_class=HelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", title="Commands")

    # Activate
    activate_parser = subparsers.add_parser(
        "activate", help="Activate the XDriver", formatter_class=HelpFormatter
    )

    # Force activate
    activate_parser.add_argument(
        "--force",
        action="store_true",
        help="Force activation (override version checks)",
    )

    # Deactivate
    deactivate_parser = subparsers.add_parser(
        "deactivate", help="Deactivate the XDriver", formatter_class=HelpFormatter
    )

    args = parser.parse_args()
    activator = Activator()

    if args.command == "activate":
        status, message = activator.activate(force=args.force)
        if not status:
            logger.warning(message)
        else:
            logger.info(message)

        if "not compatibile with XDriver" in message:
            logger.warning("Tip: You can use the --force flag for forced activation.")

    elif args.command == "deactivate":
        status, message = activator.deactivate()
        if not status:
            logger.warning(message)
        else:
            logger.info(message)

    else:
        parser.print_help()
