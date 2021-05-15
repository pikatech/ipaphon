"""
Configuration settings are collected in the file
'config.json' in the main directory and parsed
with this module.
"""
import json
import sys
from os.path import exists
from typing import Any, Dict

CONFIG = "config.json"


def read_config() -> Dict[str, Any]:
    """
    Read the configuration file of the app.

    Returns
    -------
    Dict[str, Any]
        The configuration settings
    """
    if exists(CONFIG):
        with open(CONFIG) as config:
            conf = json.load(config)
    else:
        print("Could not find configuration file {0}.".format(CONFIG))
        sys.exit(1)
    return conf
