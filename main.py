def quarter_round(a, b, c, d):
    # 0xFFFFFFFF is essentially a 32 bit number that is made only of 1s
    # It is used to prevent the number from overflowing the 32 bits
    # C language would truncate the overflowing value to fit in the 32 bit window
    # Python would NOT!, it would grow to a 64 bit number.
    # According to RFC 8439 we only want 32 bits
    a = (a + b) & 0xFFFFFFFF
    # No risk of overflowing from XOR
    d = (d ^ a)
    # RFC says d <<<= 16;
    #
    d = (d << 16 | d >> 16) & 0xFFFFFFFF
    c = (c + d) & 0xFFFFFFFF
    b = (b ^ c)
    b = (b << 12 | b >> 20) & 0xFFFFFFFF
    a = (a + b) & 0xFFFFFFFF
    d = (d ^ a)
    d = (d << 8 | d >> 24) & 0xFFFFFFFF
    c = (c + d) & 0xFFFFFFFF
    b = (b ^ c)
    b = (b << 7 | b >> 25) & 0xFFFFFFFF
    return a, b, c, d


def QUARTERROUND(a, b, c, d, chacha_state):
    new_a, new_b, new_c, new_d = quarter_round(chacha_state[a], chacha_state[b], chacha_state[c], chacha_state[d])
    chacha_state[a] = new_a
    chacha_state[b] = new_b
    chacha_state[c] = new_c
    chacha_state[d] = new_d
    return chacha_state

# a, b, c, d = quarter_round(0x11111111, 0x01020304, 0x9b8d6f43, 0x01234567)
# print(hex(a), hex(b), hex(c), hex(d))

def print_chacha_state(chacha_state):
    for i in chacha_state:
        print(hex(i))


chacha_state = [0x879531e0, 0xc5ecf37d, 0x516461b1, 0xc9a62f8a,
                0x44c20ef3, 0x3390af7f, 0xd9fc690b, 0x2a5f714c,
                0x53372767, 0xb00a5631, 0x974c541a, 0x359e9963,
                0x5c971061, 0x3d631689, 0x2098d9d6, 0x91dbd320]

QUARTERROUND(2, 7, 8, 13, chacha_state)
print_chacha_state(chacha_state)


# Initial chacha state
# cccccccc  cccccccc  cccccccc  cccccccc
# kkkkkkkk  kkkkkkkk  kkkkkkkk  kkkkkkkk
# kkkkkkkk  kkkkkkkk  kkkkkkkk  kkkkkkkk
# bbbbbbbb  nnnnnnnn  nnnnnnnn  nnnnnnnn
# c=constant k=key b=blockcount n=nonce


# For one round 
# Column rounds
QUARTERROUND(0, 4, 8, 12, chacha_state)
QUARTERROUND(1, 5, 9, 13, chacha_state)
QUARTERROUND(2, 6, 10, 14, chacha_state)
QUARTERROUND(3, 7, 11, 15, chacha_state)
# Diagonal rounds
QUARTERROUND(0, 5, 10, 15, chacha_state)
QUARTERROUND(1, 6, 11, 12, chacha_state)
QUARTERROUND(2, 7, 8, 13, chacha_state)
QUARTERROUND(3, 4, 9, 14, chacha_state)

print_chacha_state(chacha_state)
