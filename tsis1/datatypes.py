"""
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
"""

a = memoryview(bytes(6))
print(a)
print(type(a))

# Specific data type
b = dict(name = "Maksot", age= 18)
print(b)
print(type(b))