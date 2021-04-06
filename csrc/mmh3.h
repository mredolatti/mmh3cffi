uint32_t murmurhash3_32_x86(const unsigned char* key, int len, int32_t seed);
void murmurhash3_128_64(const void* key, const int len, const uint32_t seed, void* out);
