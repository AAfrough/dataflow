from src.database.loader import get_city


def test_get_city():
    city = get_city("Tehran")

    assert city["name"] == "Tehran"
    assert city["id"] == 1
    assert city["latitude"] != 0
    assert city["longitude"] != 0