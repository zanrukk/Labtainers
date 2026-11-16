
#!/usr/bin/env python3

import subprocess

PCAP_FILE = "/taps/lan.pcap"
DOH_RESOLVER = "cloudflare-dns.com"

# Students should adjust this value based on their PCAP analysis.
THRESHOLD = 2.0

def extract_doh_connections(pcap_file, resolver):
    """
    Extract TLS connections associated with the DoH resolver.

    TODO:
    1. Use tshark to read the PCAP file.
    2. Filter TLS handshakes using the resolver hostname.
    3. Extract timestamps and TCP stream IDs.
    4. Return the extracted connections.
    """
    pass


def detect_suspicious_activity(connections, threshold):
    """
    Detect potentially suspicious DoH connection patterns.

    TODO:
    1. Sort connections by timestamp.
    2. Calculate intervals between consecutive connections.
    3. Compare intervals against the student-selected threshold.
    4. Identify and report suspicious activity.
    """
    pass


def main():
    # TODO 1: Select a threshold based on your PCAP analysis.

    # TODO 2: Extract DoH connections.
    connections = extract_doh_connections(PCAP_FILE, DOH_RESOLVER)

    # TODO 3: Detect potentially suspicious activity.
    detect_suspicious_activity(connections, THRESHOLD)


if __name__ == "__main__":
    main()
