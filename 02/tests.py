from main import is_valid_id_star_one, is_valid_id_star_two, star_one, star_two

class TestStarOne:
    def test_is_valid_id_star_one(self):
        result = is_valid_id_star_one('11')
        assert result == True

        result = is_valid_id_star_one('12')
        assert result == False

        result = is_valid_id_star_one('123123')
        assert result == True

class TestStarTwo:
    def test_is_valid_id_star_two(self):
        result = is_valid_id_star_two('12312312312')
        assert result == False

        result = is_valid_id_star_two('123123123')
        assert result == True

        result = is_valid_id_star_two('1188511885')
        assert result == True

        result = is_valid_id_star_two('2121212121')
        assert result == True

        result = is_valid_id_star_two('2121212124')
        assert result == False

    def test_star_two(self):
        result = star_two(['11-22'])
        assert result == 11 + 22

        result = star_two(['95-115'])
        assert result == 99 + 111

        result = star_two(['998-1012'])
        assert result == 999 + 1010

        result = star_two(['222220-222224'])
        assert result == 222222

        result = star_two(['1698522-1698528'])
        assert result == 0

        result = star_two(['446443-446449'])
        assert result == 446446

        result = star_two(['38593856-38593862'])
        assert result == 38593859

        result = star_two(['565653-565659'])
        assert result == 565656

        result = star_two(['824824821-824824827'])
        assert result == 824824824

        result = star_two(['2121212118-2121212124'])
        assert result == 2121212121
