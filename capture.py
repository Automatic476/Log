import pandas as pd
from scapy.all import rdpcap

def process_packets(capture_file):
    # Load packet capture file
    packets = rdpcap(capture_file)

    # Process packets
    data = []
    for packet in packets:
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            # Example coordinates (replace with actual logic if needed)
            src_coords = {'lat': 36.0726, 'lng': -79.7920}  # Example for Guilford County
            dst_coords = {'lat': 36.0726, 'lng': -79.7920}  # Example for Guilford County
            data.append({
                'src_ip': src_ip,
                'dst_ip': dst_ip,
                'src_lat': src_coords['lat'],
                'src_lng': src_coords['lng'],
                'dst_lat': dst_coords['lat'],
                'dst_lng': dst_coords['lng']
            })

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to JSON for use in visualization
    df.to_json('network_data.json', orient='records')

if __name__ == '__main__':
    process_packets('capture.pcap')
