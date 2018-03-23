from FilterDS import FilterDS

def test_filter_with_no_filters():
    filter = FilterDS()
    assert None == filter.size
    assert None == filter.style

def test_filter_with_package_filter():
    filter = FilterDS(size='keg')
    assert 'keg' == filter.size
    assert None == filter.style

def test_filter_with_style_filter():
    filter = FilterDS(style='porter')
    assert None == filter.size
    assert 'porter' == filter.style

def test_filter_with_both_filters():
    filter = FilterDS(size='keg', style='porter')
    assert 'keg' == filter.size
    assert 'porter' == filter.style