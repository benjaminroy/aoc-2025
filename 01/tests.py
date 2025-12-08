from main import star_one, star_two

class TestDayOne:
    def test_star_two(self):
        result = star_two(['R49'])
        assert result == 0

        result = star_two(['R49', 'R1'])
        assert result == 1

        result = star_two(['R50'])
        assert result == 1
        
        result = star_two(['R60'])
        assert result == 1

        result = star_two(['R150'])
        assert result == 2

        result = star_two(['R550'])
        assert result == 6

        result = star_two(['L49'])
        assert result == 0

        result = star_two(['L50'])
        assert result == 1

        result = star_two(['L149'])
        assert result == 1

        result = star_two(['L150'])
        assert result == 2

        result = star_two(['L151'])
        assert result == 2

        result = star_two(['L249'])
        assert result == 2

        result = star_two(['L550'])
        assert result == 6

        result = star_two(['L200', 'R200', 'L200', 'R200'], 0)
        assert result == 8

        result = star_two(['L68', 'L30', 'R48', 'L5', 'R60'])
        assert result == 3
