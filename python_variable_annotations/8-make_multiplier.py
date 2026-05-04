#!/usr/bin/env python3
"""8-make_multiplier.py"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """def making multiplayer"""
    def multiplier_func(number: float) -> float:
        """def multiplier"""
        return number * multiplier
    return multiplier_func
