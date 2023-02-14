import time
from cobs import cobs
import serial


class Serlink:
    def __init__(self, port, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        self.dt_encode = 0
        self.dt_decode = 0

    def write(self, data: bytes):
        t1 = time.perf_counter()
        data_enc = cobs.encode(data) + b"\x00"
        t2 = time.perf_counter()
        self.dt_encode = (t2-t1)
        self.ser.write(data_enc)

    def read(self):
        data_enc = self.ser.read_until(b"\x00")
        t1 = time.perf_counter()
        data = cobs.decode(data_enc[:-1])
        t2 = time.perf_counter()
        self.dt_decode = (t2-t1)
        print(f"Got: {data}")
        return data
