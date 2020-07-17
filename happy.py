#!/usr/bin/env python3

import board
import time

# configure spi pins
spi = board.SPI()
spi.try_lock()
spi.configure(1000000)

# segment mappings
#      0b_gfedcba
segH = 0b01110110
segA = 0b01110111
segP = 0b01110011
segY = 0b01100110
seg_ = 0b00000000
seg3 = 0b01001111
seg0 = 0b00111111
segt = 0b01111000
segh = 0b01110100

while True:
  for digit in [segH, segA, segP, segP, segY, seg_, seg3, seg0, segt, segh, seg_, seg_, seg_]:
    spi.write([digit])
    time.sleep(0.3)
    spi.write([seg_])
    time.sleep(0.05)
