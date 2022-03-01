import os
from typing import Any

from flask import Flask


def get_config_item_as_bool(app: Flask, name, default: Any = None) -> bool:
    ret = get_config_item(app, name, default)

    if isinstance(ret, str):
        ret = int(ret)
        if ret == 1:
            ret = True
        else:
            ret = False

    return ret


def get_config_item(app: Flask, name, default: Any = None, allow_empty=False) -> str:
    result = None
    # prefer env vars for item
    result = os.environ.get(name, None)
    if result:
        app.logger.info(f"Using {name} from os.environ: " + result)
        return result

    # then try app.config
    result = app.config.get(name, None)
    if result:
        app.logger.info(f"Using {name} from app.config: " + result)
        return result

    if (not allow_empty) and (not default):
        # check if it's empty
        raise ValueError(f"You must set '{name}' in config.yml or env vars!"
                         f"HALTING! This service depends on {name}!")
    else:
        return default
