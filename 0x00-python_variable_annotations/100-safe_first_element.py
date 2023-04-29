#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# unkown input type
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ retirn element or null """
    if lst:
        return lst[0]
    else:
        return None
