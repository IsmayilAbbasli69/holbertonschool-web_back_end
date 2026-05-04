#!/usr/bin/env python3
"""7-to_kv.py"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """to_kv def"""
    return (k, float(v**2))
