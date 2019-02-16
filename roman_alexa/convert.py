from collections import OrderedDict

ROMAN_NUMERALS = OrderedDict(
    [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("V", 4),
        ("I", 1),
    ]
)


def arab_to_roman(n: int) -> str:
    """
    Convert arab to roman numeral.

    :param int n: The input number as a arab numeral
    :return: the roman numeral
    :rtype: str
    :raises TypeError: if the input number is not an int

    Get roman numeral for arab number:
        >>> arab_to_roman(1350)
        'MCCCL'

    Return empty string for 0 as there is no roman numeral for it:
        >>> arab_to_roman(0)
        ''

    Prefix with '-' for negative input numbers:
        >>> arab_to_roman(-1350)
        '-MCCCL'

    Input number has to be an integer:
        >>> arab_to_roman(1350.0)
        Traceback (most recent call last):
            ...
        TypeError: can't multiply sequence by non-int of type 'float'

    """

    roman = ""
    if n < 0:
        roman = "-"
        n = abs(n)

    if n == 0:
        return ""
    else:
        for sym, val in ROMAN_NUMERALS.items():
            cnt, n = divmod(n, val)
            roman += cnt * sym

    return roman


def roman_to_arab(s: str) -> int:
    """
    Convert roman to arab.

    :param str s: The input number as a roman numeral string
    :return: the arab numeral
    :rtype: int
    :raises ValueError: if the input numeral string contains non uppercase roman symbols

    :Example:

    Get arab number for roman numeral:
        >>> roman_to_arab('MCCCL')
        1350

    Return 0 for empty roman numeral string '' (to be consistent with arab_to_roman(0)):
        >>> roman_to_arab('')
        0

    Handle negative roman numerals:
        >>> roman_to_arab('-MCCCL')
        -1350

    Roman numeral string has to consist of uppercase roman symbols only:
        >>> roman_to_arab('mcA')
        Traceback (most recent call last):
            ...
        ValueError: Invalid symbol in roman numeral string
    """

    # convert to uppercase to support lower and mixed case: "MccLx"
    s = s.upper()

    arab = 0
    neg = False
    if s.startswith("-"):
        neg = True
        s = s[1:]

    while s:
        for sym, val in ROMAN_NUMERALS.items():
            if s.startswith(sym):
                arab += val
                s = s[len(sym) :]
                break
        else:
            raise ValueError("Invalid symbol in roman numeral string")

    if neg:
        return -arab
    else:
        return arab
