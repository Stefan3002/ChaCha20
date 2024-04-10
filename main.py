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

# Example usage:
a, b, c, d = quarter_round(0x11111111, 0x01020304, 0x9b8d6f43, 0x01234567)
print(hex(a), hex(b), hex(c), hex(d))