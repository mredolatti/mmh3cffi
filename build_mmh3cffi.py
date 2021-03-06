"""FFI build script."""
from cffi import FFI

FFI_BUILDER = FFI()

HEADER = 'uint32_t murmurhash3_32_x86(const unsigned char* key, int len, int32_t seed);'

FFI_BUILDER.cdef(HEADER)
FFI_BUILDER.set_source(
    'mmh3cffi._cimpl',
    '',
    sources=['csrc/mmh3.c'],
    include_dirs=['./csrc']
)

if __name__ == '__main__':
    FFI_BUILDER.compile()
