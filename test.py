# coding: utf8
"""
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-07
"""

import sys

sys.dont_write_bytecode = True

import setuptools

if __name__ == "__main__":
    print()
    for i in setuptools.find_packages():
        print(i)
