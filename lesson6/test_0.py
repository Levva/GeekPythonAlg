import sys
import ctypes
import struct

a = 5
b = 125.54
c = 'Hello World!'

print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a)), sys.getsizeof(a))
print(struct.unpack('LLLcc', ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))

print('*' * 50)

print(id(b))
print(sys.getsizeof(b))

print(ctypes.string_at(id(b)), sys.getsizeof(b))
print(struct.unpack('LLLl', ctypes.string_at(id(b), sys.getsizeof(b))))
print(id(float))

print('*' * 50)

print(id(c))
print(sys.getsizeof(c))

print(ctypes.string_at(id(c)), sys.getsizeof(c))
print(struct.unpack('LLLLLLLLLc', ctypes.string_at(id(c), sys.getsizeof(c))))
print(id(float))