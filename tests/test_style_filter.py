from abv.beer import Beer
from abv.style_filter import StyleFilter
from abv.yes_filter import YesFilter


def test_name_filter_match():
    b = Beer('bud', '1/2 keg', 'lager', '2.00', '1.00')
    f = StyleFilter(YesFilter(), 'lager')
    assert f.is_match(b) is True


def test_name_filter_no_match():
    b = Beer('bud', '1/2 keg', 'lager', '2.00', '1.00')
    f = StyleFilter(YesFilter(), 'stout')
    assert f.is_match(b) is False
    