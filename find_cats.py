import os

from settings import CAT_DIRS, CAT_EXTS, STATIC_ROOT


def _is_hidden(filename):
    return filename.startswith(".")


def _cleanup_hidden_dirs(dirnames):
    dirnames[:] = [dirname for dirname in dirnames if not _is_hidden(dirname)]


def _get_ext(filename):
    return os.path.splitext(filename)[1]


def _cats_from_dir(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        _cleanup_hidden_dirs(dirnames)
        yield from (os.path.relpath(os.path.join(dirpath, filename), STATIC_ROOT) for filename in filenames
                    if not _is_hidden(filename) and _get_ext(filename) in CAT_EXTS)


def find_cats():
    def gen():
        for dir in CAT_DIRS:
            yield from _cats_from_dir(dir)
    return list(gen())
