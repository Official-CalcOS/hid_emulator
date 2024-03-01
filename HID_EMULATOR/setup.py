from setuptools import setup, Extension

setup(
    name='hid_emulator',
    version='1.0.0',
    description='A Python Package written in C++ for emulating HID (human interface devices) programatically',
    ext_modules=[Extension('hid_emulator', ['hid_emulator.py', 'HID_Emulator.dll'])],
    packages=['HID_EMULATOR'],
)