from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities'
]

setup(
    name='mmh3cffi',
    version='0.1.2',
    description='CFFI interface to murmurhash3/32 from aappleby/smhasher',
    license='Apache 2.0',
    author='Split software',
    author_email='python@split.io',
    url='https://github.com/splitio/mmh3cffi',
    packages=find_packages(exclude=['test, csrc']),
    setup_requires=['cffi>=1.4.0', 'pytest-runner'],
    install_requires=['cffi>=1.4.0', 'future'],
    tests_require=['pytest'],
    cffi_modules=['build_mmh3cffi.py:FFI_BUILDER']
)
