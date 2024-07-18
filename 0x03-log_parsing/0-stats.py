#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
    - After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        - Total file size: File size: <total size> where <total size>
        is the sum of all previous <file size> (see input format above)
        - Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        - if a status code doesn’t appear or is not an integer,
        don’t print anything for this status code
        - format: <status code>: <number>
    status codes should be printed in ascending order
"""
import sys
import signal
import re

STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

ipv4_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
date_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}"
tcp_pattern = r"GET /projects/260 HTTP/1.1"
status_code_pattern = r"\d{3}"
file_size_pattern = r"\d+"
PATTERN = r"{} - \[{}\] \"{}\" ({}) ({})".format(
    ipv4_pattern, date_pattern, tcp_pattern,
    status_code_pattern, file_size_pattern
)

count = 0
track_status_code = dict()
total_file_size = 0


def display_stats():
    sys.stdout.write("File size: {}\n".format(total_file_size))
    status_list = list(track_status_code.items())
    status_list.sort(key=lambda x: x[0])
    for status in status_list:
        sys.stdout.write("{}: {}\n".format(status[0], status[1]))


def handle_sigint(signal_number, frame):
    display_stats()
    sys.stdout.flush()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)
while True:
    line = sys.stdin.readline()

    if line == '':
        break

    pattern = re.compile(PATTERN)
    match = re.match(pattern, line)

    if not match:
        continue

    status_code = int(match.group(1))
    file_size = int(match.group(2))

    if status_code not in STATUS_CODES:
        continue

    if status_code in track_status_code:
        track_status_code[status_code] += 1
    else:
        track_status_code[status_code] = 1

    total_file_size += file_size
    count += 1

    if count == 10:
        display_stats()
        count = 0
