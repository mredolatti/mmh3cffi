"""FFI build script."""
import os
from cffi import FFI


with open(os.path.join("csrc", "mmh3.h"), 'r') as f: HEADER = f.read()

FFI_BUILDER = FFI()
FFI_BUILDER.cdef(HEADER)
FFI_BUILDER.set_source(
    'mmh3cffi._cimpl',
    '#include "mmh3.h"',
    sources=[os.path.join('csrc', 'mmh3.c')],
    include_dirs=['csrc'],
    extra_compile_args=['-std=c99']
)

if __name__ == '__main__':
    FFI_BUILDER.compile()
