from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello world!\n"
msvcrt.printf("Testing: %s", message_string)
msvcrt.printf("Testing: %s", message_string)

print(c_int())
c_char_p("Hello world!")