from FilterDS import FilterDS

def test_filter_with_no_filters():
    filter = FilterDS()
    assert None == filter.package
    assert None == filter.style

def test_filter_with_package_filter():
    filter = FilterDS(package='keg')
    assert 'keg' == filter.package
    assert None == filter.style

def test_filter_with_style_filter():
    filter = FilterDS(style='porter')
    assert None == filter.package
    assert 'porter' == filter.style

def test_filter_with_both_filters():
    filter = FilterDS(package='keg', style='porter')
    assert 'keg' == filter.package
    assert 'porter' == filter.style