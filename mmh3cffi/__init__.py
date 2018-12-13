"""Python frontend for the C implementation of murmurhash3."""
from builtins import bytes
from mmh3cffi._cimpl import ffi, lib

def hash_str(to_hash, seed=0):
    """
    Calculate murmur3/32 hash of incoming string and seed.

    :param to_hash: String to hash
    :type to_hash: str

    :param seed: Seed to use as a hashing starting point.
    :type seed: int
    """
    as_bytes = to_hash.encode('utf8')
    const_char_pointer = ffi.new('const unsigned char[]', as_bytes)
    result = lib.murmurhash3_32_x86(const_char_pointer, len(as_bytes), seed)
    return result
