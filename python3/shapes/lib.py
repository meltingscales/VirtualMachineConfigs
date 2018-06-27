from functools import lru_cache


@lru_cache(maxsize=None)
def read_file_cached(path: str) -> []:
    return open(path, 'r').readlines()


def log_to_file(path, s):
    with open(path, 'w+') as f:

        if isinstance(s, str):
            f.write(s)

        elif isinstance(s, list) or isinstance(s, tuple):
            for item in s:
                f.write(item + '\n')
