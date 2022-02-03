import os
from typing import Any


def get_config_item(app, name, default: Any = None) -> str:
    result = None
    # prefer env vars for item
    result = os.environ.get(name, None)
    if result:
        print(f"Using {name} from os.environ: " + result)
        return result

    # then try app.config
    result = app.config.get(name, None)
    if result:
        print(f"Using {name} from app.config: " + result)
        return result

    if default is None:
        # check if it's empty
        raise ValueError(f"You must set '{name}' in config.yml or env vars!"
                         f"HALTING! This service depends on {name}!")
    else:
        return default
