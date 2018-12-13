from setuptools import setup, find_packages

setup(
    name='mmh3cffi',
    version='0.1.1',
    packages=find_packages(exclude=['test, csrc']),
    setup_requires=['cffi>=1.4.0'],
    install_requires=['cffi>=1.4.0'],
    cffi_modules=['build_mmh3cffi.py:FFI_BUILDER']
)
