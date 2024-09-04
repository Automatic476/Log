Capture Traffic:

sudo tcpdump -i <interface> -w capture.pcap

Run the Complete Setup
Capture Traffic: Run the tcpdump command on your network interface to capture traffic.

Process Data:

python capture.py
This generates network_data.json.

Serve Files: Host your index.html and script.js files using a simple HTTP server (e.g., using Python's http.server):

python -m http.server 8000