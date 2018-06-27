from functools import lru_cache


@lru_cache(maxsize=None)
def read_file_cached(path: str) -> []:
    return open(path, 'r').readlines()
