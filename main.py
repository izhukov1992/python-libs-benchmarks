from confluent import test_confluent_complex

if __name__ == "__main__":
    # Results for Python 3.11.1 (takes 24Gb in total)
    test_confluent_complex(True, True, 5000000, 1000000)    # produce: 32.55, complex: 50.00    # produce: 36.05, complex: 52.27    # produce: 42.99, complex: 59.46    # produce: 33.75, complex: 52.56    # produce: 46.00, complex: 65.03
    test_confluent_complex(True, True, 5000000, 100000)     # produce: 35.94, complex: 44.68    # produce: 32.98, complex: 42.30    # produce: 37.96, complex: 45.81    # produce: 34.12, complex: 43.43    # produce: 37.42, complex: 45.49
    test_confluent_complex(True, True, 5000000, 10000)      # produce: 36.39, complex: 49.35    # produce: 36.43, complex: 49.20    # produce: 36.81, complex: 49.19    # produce: 37.72, complex: 49.10    # produce: 39.67, complex: 51.17
    test_confluent_complex(True, True, 5000000, 1000)       # produce: 57.30, complex: 63.77    # produce: 57.01, complex: 61.64    # produce: 57.17, complex: 64.30    # produce: 56.23, complex: 63.40    # produce: 55.44, complex: 63.13
    test_confluent_complex(True, True, 5000000, 100)        # produce: 119.73, complex: 128.04  #                                   # produce: 100.90, complex: 115.07  # produce: 109.15, complex: 121.46  # produce: 107.52, complex: 121.96

    test_confluent_complex(True, True, 5000000, 1000)       # produce: 54.94, complex: 62.28
    test_confluent_complex(True, True, 5000000, 100)        # produce: 111.39, complex: 124.13
    test_confluent_complex(True, True, 5000000, 1000000)    # produce: 37.00, complex: 55.02
    test_confluent_complex(True, True, 5000000, 100000)     # produce: 37.50, complex: 46.57
    test_confluent_complex(True, True, 5000000, 10000)      # produce: 37.22, complex: 50.01
