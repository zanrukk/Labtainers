#!/bin/bash

set -e

TARGET="https://example.com/"
DOH_URL="https://cloudflare-dns.com/dns-query"

echo "=================================="
echo " DoH Detection Lab - Traffic Test"
echo "=================================="

echo
echo "[1] Generating ordinary HTTPS traffic..."

for i in $(seq 1 3); do
    echo "HTTPS request $i"
    curl -4 -sS -o /dev/null "$TARGET"
    sleep 2
done

echo
echo "[2] Generating legitimate DoH traffic..."

for i in $(seq 1 3); do
    echo "Legitimate DoH request $i"
    curl -4 -sS -o /dev/null --doh-url "$DOH_URL" "$TARGET"
    sleep 5
done

echo
echo "[3] Generating high-frequency DoH traffic..."

for i in $(seq 1 10); do
    echo "High-frequency DoH request $i"
    curl -4 -sS -o /dev/null --doh-url "$DOH_URL" "$TARGET"
    sleep 0.2
done

echo
echo "Traffic generation completed."
