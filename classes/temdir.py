from pathlib import Path
from typing import Optional

from schemas.essential_types import StrPathOrNone
from utils.file_utils import create_temp_dir
from utils.file_utils import remove_dir


class TempDir:
    """
    Context class for temporarily directories handling
    Optional simple implementation of tempfile.TemporaryDirectory
    """

    def __init__(self, base_path: StrPathOrNone = None):
        self.base_path = base_path
        self._temp_dir: Optional[Path] = None

    def __enter__(self) -> 'TempDir':
        self.create()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.remove()

    def create(self):
        # Create temp dir (internal usage and fine grain control)
        self._temp_dir = create_temp_dir(self.base_path)
        return self._temp_dir

    def remove(self):
        # Remove temp dir (internal usage and fine grain control)
        if self._temp_dir is not None:
            if self._temp_dir.is_dir():
                remove_dir(self._temp_dir)
            self._temp_dir = None

    @property
    def dir(self) -> Path:
        if self._temp_dir is None:
            raise ValueError('Temporary dir is not created')
        return self._temp_dir


class NamedTempDir:
    """Dir name contextmanager implementation
    Wrap TempDir with self context manager
    """

    def __init__(self, base_path: StrPathOrNone = None):
        self.temp_dir = TempDir(base_path)

    def __enter__(self) -> Path:
        self.temp_dir.__enter__()
        return self.temp_dir.dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.temp_dir.__exit__(exc_type, exc_val, exc_tb)
