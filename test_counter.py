from counter import count_on_bits

def test_counter():
    assert(count_on_bits(2) == 1)
    assert(count_on_bits(3) == 2)
    assert(count_on_bits(256) == 1)

