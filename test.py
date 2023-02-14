import serlink
import random
import json


def print_hex(array):
    txt = " ".join([f"{x:02x}" for x in array])
    print(txt)


def test_efficiency():
    link = serlink.Serlink("COM158")
    encode_host_us = []
    decode_host_us = []
    data_length = []
    n_tests = 2000
    n_max = 1024

    for k in range(n_tests):
        n = random.randint(1, n_max)
        data = bytes([random.randint(0, 255) for _ in range(n)])
        link.write(data)
        data_back = link.read()

        print_hex(data)
        print_hex(data_back)

        quit()
        # print_hex(data)
        # print_hex(data_back)

        encode_host_us.append(link.dt_encode * 1e6)
        decode_host_us.append(link.dt_decode * 1e6)
        data_length.append(n)
    with open("results.txt", "w") as f:
        json.dump({
            "encode_host_us": encode_host_us,
            "decode_host_us": decode_host_us,
            "data_length": data_length
        }, f, indent=2)


def main():
    test_efficiency()


if __name__ == "__main__":
    main()
