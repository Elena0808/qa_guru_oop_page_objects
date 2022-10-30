from pathlib import Path
import files_for_test


def abs_path(relative_path: str):
    return str(Path(files_for_test.__file__).parent.joinpath(relative_path).absolute())
