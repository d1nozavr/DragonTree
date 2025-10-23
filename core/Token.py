"""
DragonTree
Token
"""

class Token:
    def __init__(self, _type, _value=None):
        self._type = _type
        self._value = _value

    def __repr__(self):
        if self._value:
            return f"Token({self._type}, {self._value})"

        return f"Token({self._type})"
