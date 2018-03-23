from beer import Beer
from name_filter import NameFilter
from yes_filter import YesFilter

def test_name_filter_match():
    b = Beer('bud', '1/2 keg', 'lager', '2.00', '1.00')
    f = NameFilter(YesFilter(), 'bud')
    assert f.is_match(b) is True


def test_name_filter_no_match():
    b = Beer('bud', '1/2 keg', 'lager', '2.00', '1.00')
    f = NameFilter(YesFilter(), 'bud light')
    assert f.is_match(b) is False
