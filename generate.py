# Copyright (c) 2024 Yuichi Ishida
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php

import sys

LATEX_MAX_ARGS = 9


def nest_optional_args(c: str, n: int, i: int = 1):
    """
    nest_optional_args(c='a', n=3)で文字列{\IfValueT{#1}{#1} {\IfValueT{#2}{#2} {\IfValueT{#3}{#3} {\Phi}}}} を生成する。
    """
    if not (0 <= n <= LATEX_MAX_ARGS):
        raise ValueError(f"n must be between 0 and {LATEX_MAX_ARGS}")
    if not (1 <= i <= n):
        raise ValueError(f"i must be between 1 and n")
    if i == n:
        return "{\\IfValueT{"+f"#{i}"+"}{"+f"#{i}"+"} "+"{"+f"{c}"+"}}"
    else:
        return "{\\IfValueT{"+f"#{i}"+"}{"+f"#{i}"+"} " + nest_optional_args(c, n, i=i+1) + "}"
