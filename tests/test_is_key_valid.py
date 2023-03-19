import typing

import pytest

from lotr.error import CustomError
from lotr.utils import is_api_key_valid


@pytest.mark.parametrize(
    "api_key, expect_valid, expect_error",
    [
        pytest.param("valid", True, False, id="valid key"),
        pytest.param("", False, True, id="empty key"),
        pytest.param(None, False, True, id="no key"),
    ],
)
def test_is_api_key_valid(api_key: typing.Optional[str], expect_valid: bool, expect_error: bool):
    if expect_error:
        with pytest.raises(CustomError):
            is_api_key_valid(api_key)
    else:
        actual = is_api_key_valid(api_key)
        assert expect_valid == actual