from pathlib import Path

import pytest

from utils.file_utils import create_temp_dir
from utils.file_utils import remove_dir


@pytest.fixture()
def temp_dir() -> Path:
    return create_temp_dir()


def write_some_data(file_name: Path, data: str):
    with open(file_name, mode='w') as f:
        f.write(data)


def test_remove_dir(temp_dir):
    assert temp_dir.is_dir(), 'Directory %s should be created' % temp_dir
    # create some nested directories
    temp_dir_1 = create_temp_dir(temp_dir)
    temp_dir_2 = create_temp_dir(temp_dir)
    write_some_data(temp_dir_1.joinpath('file_1.txt'), 'This is data for file 1')
    write_some_data(temp_dir_1.joinpath('file_2.txt'), 'This is data for file 2')
    write_some_data(temp_dir_2.joinpath('file_3.txt'), 'This is data for file 3')
    write_some_data(temp_dir_2.joinpath('file_4.txt'), 'This is data for file 4')
    remove_dir(temp_dir)
    assert not temp_dir.is_dir(), 'Directory %s should be removed' % temp_dir
