import ctypes
import os

# Load the shared library
_dll_path = os.path.join(os.path.dirname(__file__), 'HID_Emulator.dll')
_dll = ctypes.CDLL(_dll_path)

# Define the function prototype
myFunction = _dll.myFunction
myFunction.argtypes = []
myFunction.restype = None
