from pytest import mark

#we can use parametrize to run the same test case with different values
@mark.parametrize('tv_series', [
    ('Supernatural'),
    ('Riverdale'),
    ('Dark'),
    ('Ozark')
])

@mark.tvseries
def test_tv_series_showed(tv_series):
    print(f"{tv_series} will be shown on tv this week")

#the same, just using a data-driven testing approach
@mark.tvseries
def test_tv_series_showed_with_data(test_data):
    print(f"{test_data} will be shown on tv this week")

