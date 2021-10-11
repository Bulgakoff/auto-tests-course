import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert False


@pytest.mark.xfail(strict=True)
def test_not_succeed():
    assert True


@pytest.mark.skip
def test_skipped():
    assert False