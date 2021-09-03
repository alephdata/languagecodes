from typing import Optional


def normalize_code(code: Optional[str]) -> Optional[str]:
    if code is None:
        return None
    code = str(code)
    code = code.lower().strip()
    if not len(code):
        return None
    return code
