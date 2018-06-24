

def normalize_code(code):
    if code is None:
        return None
    code = str(code)
    code = code.lower().strip()
    if not len(code):
        return None
    return code
