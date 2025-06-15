from __future__ import annotations

from collections.abc import Generator
from collections.abc import Iterable
from contextlib import contextmanager
from itertools import tee
from pathlib import Path


@contextmanager
def file_modification_transaction(
    pos_args: Iterable[str], python_only: bool = True
) -> Generator[tuple[Iterable[Path], Iterable[str]], None, None]:
    paths = map(Path, pos_args)
    if python_only:
        paths1, paths2, paths3 = tee(paths)
    else:
        paths1, paths2, paths3 = tee(
            filter(lambda path: path.suffix == ".py", paths)
        )
    contents = map(Path.read_text, paths1)
    try:
        yield paths2, contents
    except BaseException:
        print("Reverting changes please wait until process is done...")
        for path, content in zip(paths3, contents):
            path.write_text(content)
        print("Changes reverted")
        raise
