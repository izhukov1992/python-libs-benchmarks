from .spavro import test_spavro


def test_avro():
    # Results for Python 3.11.1
    test_spavro(100000000)
    # test_spavro(1000)
