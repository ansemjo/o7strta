#!/usr/bin/env python3

import board
import time

# configure spi pins
spi = board.SPI()
spi.try_lock()
spi.configure(1000000)

# segment mappings
H = 0b01110110
E = 0b01111001
L = 0b00111000
O = 0b00111111
_ = 0b00000000

while True:
  for c in [H, E, L, L, O]:
    spi.write([c])
    time.sleep(0.3)
    spi.write([_])
    time.sleep(0.05)
