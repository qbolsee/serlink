import json
import numpy as np
import matplotlib.pyplot as plt


def main():
    with open("results.txt", "r") as f:
        results = json.load(f)
    encode_host_us = np.array(results["encode_host_us"], dtype=np.float64)
    decode_host_us = np.array(results["decode_host_us"], dtype=np.float64)
    data_length = np.array(results["data_length"], dtype=int)

    encode_host_us_norm = encode_host_us / data_length
    decode_host_us_norm = decode_host_us / data_length
    # print(np.mean(encode_host_us_norm), np.std(encode_host_us_norm))
    # print(np.mean(decode_host_us_norm), np.std(decode_host_us_norm))

    plt.figure()
    plt.hist(encode_host_us_norm, bins=np.linspace(0, 0.07, 64))
    # plt.hist(encode_host_us, bins=np.linspace(0, 10, 64))

    plt.figure()
    plt.hist(decode_host_us_norm, bins=np.linspace(0, 0.07, 64))
    # plt.hist(decode_host_us, bins=np.linspace(0, 10, 64))

    plt.figure()
    plt.hist(data_length, bins=np.linspace(0, 1024, 64))

    plt.show()


if __name__ == "__main__":
    main()
