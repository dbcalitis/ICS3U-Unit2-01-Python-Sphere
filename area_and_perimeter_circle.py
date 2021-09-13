#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sep 2021
# This program calculates the area and perimeter of a circle
#    with radius 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 15mm: \n")
    print("The area will be {}mm²".format(math.pi * (15 ** 2)))
    print("The perimeter will be {}mm \n".format(2 * math.pi * 15))
    print("Done")


if __name__ == "__main__":
    main()
