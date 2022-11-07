import helpers

def test_sum():
    assert helpers.calc_sleep_time(8, 32) == 512, "Should be 512"

def test_negative():
    assert helpers.calc_sleep_time(-1, 20) == -1, "Should be -1"

def test_negative_minutes():
    assert helpers.calc_sleep_time(8, -1) == -1, "Should be -1"

if __name__ == "__main__":
    test_sum()
    test_negative()
    test_negative_minutes()
    print("Everything passed")