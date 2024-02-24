# TempDir unit tests
from pathlib import Path
from typing import Optional

import pytest

from classes.temdir import NamedTempDir
from classes.temdir import TempDir


def test_tempdir():
    temp_dir: Optional[Path]
    with NamedTempDir() as temp_dir:
        nested_dir: Optional[Path]
        with TempDir(temp_dir) as nested_temp_dir_obj:
            nested_dir = nested_temp_dir_obj.temp_dir
            assert nested_temp_dir_obj.temp_dir.is_dir(), 'Nested dir does not exist'
        assert not nested_dir.is_dir(), 'Nested dir should not exist (after __exit__)'
    assert temp_dir is not None, 'Context manager returns filled Path object (None check)'

    assert isinstance(temp_dir, Path), 'Context manager returns filled Path object (class check)'
    assert not nested_dir.is_dir(), 'Nested dir does not exist'
    with pytest.raises(ValueError):
        # nested_temp_dir_obj.dir is Path sibling, so if assertion won't raise we see assertion fail check
        assert isinstance(
            nested_temp_dir_obj.temp_dir, str
        ), 'Should raise exception here so this assert should not execute successfully'
