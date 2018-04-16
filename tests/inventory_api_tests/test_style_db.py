from abv.inventory_api.style_db import StyleDB


def test_cache_has_beer():
    styles = StyleDB()
    assert styles.get_style('Nitro') == 'stout'
    assert styles.brew_db.count == 0


def test_db_has_style_and_then_cache():
    styles = StyleDB()
    tested = styles.get_style('Guinness')
    print(tested)
    assert styles.get_style('Guinness') == 'stout'
    assert styles.get_style('Guinness') == 'stout'
    assert styles.brew_db.count == 1


def test_unknown_from_db_then_cache():
    styles = StyleDB()
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.brew_db.count == 1


def test_two_against_db():
    """ Tests that if query throws error once, that it throws it again by same input """
    styles = StyleDB()
    assert styles.get_style('xyz') == "Unknown"
    assert styles.get_style('xyz') == "Unknown"
    assert styles.brew_db.count == 2
