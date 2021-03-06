# -*- coding: utf-8 -*-

import calendar


MONTH_NAME_MAP = dict(map(lambda (i, n): (i + 1, n),
                          enumerate(calendar.month_name[1:])))

MONTH_VALUE_NAME_MAP = dict(map(lambda (i, n): (n, i + 1),
                                enumerate(calendar.month_name[1:])))

MONTH_ABBR_MAP = dict(map(lambda (i, n): (i + 1, n),
                          enumerate(calendar.month_abbr[1:])))

MONTH_VALUE_ABBR_MAP = dict(map(lambda (i, n): (n, i + 1),
                          enumerate(calendar.month_abbr[1:])))

DAY_NAME_MAP = dict(map(lambda (i, n): (i + 1, n),
                        enumerate(calendar.day_name[1:])))

DAY_ABBR_MAP = dict(map(lambda (i, n): (i + 1, n),
                        enumerate(calendar.day_abbr[1:])))


__all__ = [
    'MONTH_NAME_MAP',
    'MONTH_VALUE_ABBR_MAP',
    'MONTH_ABBR_MAP',
    'MONTH_VALUE_ABBR_MAP',
    'DAY_NAME_MAP',
    'DAY_ABBR_MAP'
]
