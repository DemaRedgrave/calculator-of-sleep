import helpers

def test_sum():
    assert helpers.calc_sleep_time(8, 32) == 512, "Should be 512"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")