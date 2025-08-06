# -*- encode: utf-8 -*-

import pytest

from package_name.main import main


@pytest.fixture(scope="module")
def two_integers() -> tuple[int, int]:
    """Test data directory for this test class."""
    return 1, 2


class TestMain:
    """Test class for the main script."""

    def test_main_function(self, two_integers) -> None:
        """Test the main function with two integers."""
        a, b = two_integers
        expected_answer = 3
        assert main(a, b) == expected_answer
