import pytest

from decorators.exception_wrapper import exception_catch


class ErrorCounter:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def increment(self, *_args):
        self._count += 1


@pytest.fixture()
def error_counter():
    error_counter = ErrorCounter()
    return error_counter


def test_exception_catch(error_counter):
    @exception_catch(exception_range=(ZeroDivisionError,), exception_value=0.0, callback=error_counter.increment)
    def make_division(a, b: float):
        if b >= 100:
            raise ValueError('b argument is too much (%d)' % b)
        return a / b

    assert make_division(1, 2) == 0.5, 'Wrong calculation on step 1'
    assert error_counter.count == 0, 'No error should be catch on this step'
    assert make_division(1, 0) == 0, 'Wrong calculation on step 2'
    assert error_counter.count == 1, 'One error should be catch on this step'
    assert make_division(3, 1.5) == 2, 'Wrong calculation on step 3'
    assert error_counter.count == 1, 'One error should be catch on this step'
    with pytest.raises(ValueError):
        print(make_division(1, 100))
    assert make_division(100, 0) == 0, 'Wrong calculation on step 4'
    assert error_counter.count == 2, 'One error should be catch on this step'


def test_exception_catch_with_log(caplog):
    @exception_catch(exception_range=(ZeroDivisionError,), exception_value=None)
    def make_division_no_exception(a, b: float):
        return a / b

    assert make_division_no_exception(1, 2) == 0.5, 'Wrong calculation on step 1'
    assert len(caplog.text) == 0, 'No log records should be captured'
    assert make_division_no_exception(1, 0) is None, 'Wrong calculation on step 2'
    assert (
        caplog.text.index('Error in "make_division_no_exception" routine, details: division by zero') != -1
    ), 'Log message should contain exception log message'
