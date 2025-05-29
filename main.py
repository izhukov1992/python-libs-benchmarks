from confluent import test_confluent_complex

if __name__ == "__main__":
    # Results for Python 3.11.1 (takes 24Gb in total)
    test_confluent_complex(True, True, 5000000, 1000000)    # produce: 18.76, complex: 35.40
    test_confluent_complex(True, True, 5000000, 100000)     # produce: 18.90, complex: 36.37
    test_confluent_complex(True, True, 5000000, 10000)      # produce: 20.98, complex: 28.04
    test_confluent_complex(True, True, 5000000, 1000)       # produce: 35.95, complex: 45.44
    test_confluent_complex(True, True, 5000000, 100)        # produce: 58.36, complex: 69.15

    test_confluent_complex(True, True, 5000000, 1000)       # produce: 36.36, complex: 46.43
    test_confluent_complex(True, True, 5000000, 100)        # produce: 57.80, complex: 69.60
    test_confluent_complex(True, True, 5000000, 1000000)    # produce: 18.51, complex: 34.76
    test_confluent_complex(True, True, 5000000, 100000)     # produce: 18.94, complex: 33.51
    test_confluent_complex(True, True, 5000000, 10000)      # produce: 21.01, complex: 27.70
