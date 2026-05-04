#!/usr/bin/env python3
"""pagination"""


def index_range(page=1, page_size=10):
    """useing pagination"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
