#!/usr/bin/env python3

import re

with open("/Users/gillian/Dropbox/My Mac (gillian-FVFF9334Q6LT.local)/Documents/Using-Python-to-interact-with-the-operating-system/Final Project/syslog_sample.txt", "r") as log_file


def split_up_message(log_file):
    for row in log_file:
        ticketType = re.search(r"(INFO|ERROR)", row)
        print(ticketType[0])


def main():
    split_up_message()


if __name__ == "__main__":
    main()
