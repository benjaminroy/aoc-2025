from main import merge_ranges, star_one, star_two

class TestDayFive:
    def test_merge_ranges(self):
        result = merge_ranges(['3-5', '10-14', '16-20', '12-18'])
        assert result == ['3-5', '10-20']

        result = merge_ranges(['3-5', '5-10'])
        assert result == ['3-10']

        result = merge_ranges(['3-5', '1-10'])
        assert result == ['1-10']

        result = merge_ranges(['3-5', '4-10'])
        assert result == ['3-10']

    def test_star_one(self):
        result = star_one(['3-5', '10-14', '16-20', '12-18'], ['1', '5', '8', '11', '17', '32'])
        assert result == 3

    def test_star_two(self):
        result = star_two(['3-5', '10-14', '16-20', '12-18'])
        assert result == 14
