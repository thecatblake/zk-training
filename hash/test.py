import hashlib

def zokrates_sha256packed_bytes(a, b, c, d):
    def enc128(x): return int(x).to_bytes(16, "big", signed=False)
    msg = enc128(a) + enc128(b) + enc128(c) + enc128(d)
    assert len(msg) == 64
    return hashlib.sha256(msg).digest()

digest = zokrates_sha256packed_bytes(0,0,0,5)

h0 = int.from_bytes(digest[:16], "big")
h1 = int.from_bytes(digest[16:], "big")
print(h0, h1)