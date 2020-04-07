def hex_string_to_bytes(string='cafebabe'):  # shamelessly stolen from https://stackoverflow.com/a/5649532
    """Given a hex string return a byte string."""
    bits = b""
    for x in xrange(0, len(string), 2):
        bits += chr(int(string[x:x + 2], 16))

    return bits


def int_to_hex_string(integer=0xcafebabe):
    """Given an integer return a human readable hex string."""
    return hex(integer)[2:]


assert (int_to_hex_string(0x1234) == '1234')


def int_to_bytes(integer):
    """Given an integer return a byte string."""
    return hex_string_to_bytes(int_to_hex_string(integer))


assert (hex_string_to_bytes(int_to_hex_string(0x1234)) == '\x12\x34')


def reverse_endian_of_bytes(bytestring=b'\xca\xfe\xba\xbe'):
    """Reverse the endianness of a byte string."""
    # bits = b""
    # for x in xrange(len(bytestring), 0, -2):
    #     bits += bytestring[x:x + 1]
    #
    return bytestring[::-1]


assert (reverse_endian_of_bytes('\xca\xfe\xba\xbe') == '\xbe\xba\xfe\xca')
assert (reverse_endian_of_bytes(reverse_endian_of_bytes('\x12\x34\x56\x78')) == '\x12\x34\x56\x78')
