from array import *

x = array("i", [1, 2, 3, 4, 5, 6])
byte_string = x.tobytes()
clean_str = str(byte_string).split(
    "\\x"
)  # the converted string contains '\\x' character which is unnecessary
print("".join(clean_str))
