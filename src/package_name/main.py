# -*- encode: utf-8 -*-


def main(
    a: int,
    b: int,
) -> int:
    """Function to return the sum of two integers.

    Args:
        a: The first integer to add.
        b: The second integer to add.

    Returns:
        An **integer** whose value is the sum of the two integers.

    Examples:
        Positive integers:
            ```python
            >>> main(1, 2)
            3
            ```

        Mixed signed integers:
            ```python
            >>> main(-1, 2)
            1
            ```
    """
    return a + b
