"This is the filter factor that turns filter data strcutures into filters. "
from abv.size_filter import SizeFilter
from abv.name_filter import NameFilter
from abv.yes_filter import YesFilter
from abv.style_filter import StyleFilter
from abv.availability_filter import AvailabilityFilter

#pylint: disable=missing-docstring
def build(filter_ds):
    recursive_filter = YesFilter()
    if filter_ds.size is not None:
        recursive_filter = SizeFilter(recursive_filter, filter_ds.size)
    if filter_ds.name is not None:
        recursive_filter = NameFilter(recursive_filter, filter_ds.name)
    if filter_ds.style is not None:
        recursive_filter = StyleFilter(recursive_filter, filter_ds.style)
    if filter_ds.availability is not None:
        recursive_filter = AvailabilityFilter(recursive_filter, filter_ds.availability)
    return recursive_filter
