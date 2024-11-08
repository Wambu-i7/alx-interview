#!/usr/bin/env python3
"""
This script reads log data from stdin line by line, parsing each line
for specific metrics.
Metrics include:
  - Total file size, which accumulates the sum of file sizes from all
  parsed lines
  - Number of occurrences of specific HTTP status codes

Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
    <file size>

After every 10 lines or when interrupted with CTRL + C, the script outputs:
  - Total file size (sum of all <file size> values from valid lines)
  - Number of lines for each status code (only codes that appear are printed)
"""

import sys
import signal

# Initialize metrics
total_file_size = 0
status_counts = {code: 0 for code in (200, 301, 400, 401, 403, 404, 405, 500)}
line_count = 0

def print_stats():
    """Prints the computed statistics: total file size and status code counts."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """Parses a log line and updates the metrics if the line matches the format."""
    global total_file_size

    parts = line.split()
    if len(parts) < 7:
        return  # Skip lines that do not meet the minimum length requirement

    try:
        # Extract status code and file size from the end of the line
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        if status_code in status_counts:
            status_counts[status_code] += 1
        total_file_size += file_size
    except (ValueError, IndexError):
        # Skip lines that do not match the expected format for status_code or file_size
        pass

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) to print statistics before exiting."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process stdin line by line
for line in sys.stdin:
    parse_line(line.strip())
    line_count += 1

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats if input ends
print_stats()
