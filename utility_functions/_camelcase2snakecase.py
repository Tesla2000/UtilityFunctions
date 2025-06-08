from __future__ import annotations

import re


def camelcase2snakecase(camelcase_string: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camelcase_string).lower()
