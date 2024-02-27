from isPrime import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(-5) == False
    assert is_prime(-60) == False
    assert is_prime(23) == True
    assert is_prime(29) == True