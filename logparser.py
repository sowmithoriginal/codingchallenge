import csv
from collections import defaultdict

# Function to load tag mappings from the lookup table
def load_tag_mappings(lookup_file):
    tag_mapping = {}
    with open(lookup_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Extract and clean up dstport, protocol, and tag values
            dstport = row['dstport'].strip()
            # Convert protocol to lowercase for case-insensitive matching
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            # Mapping
            tag_mapping[(dstport, protocol)] = tag
    return tag_mapping

# Function to parse flow log entries and match with tags
def process_flow_logs(flow_file, tag_mapping):
    tag_count = defaultdict(int)
    port_protocol_count = defaultdict(int)

    with open(flow_file, 'r') as file:
        for line in file:
            # Split the line into columns and extract relevant information
            columns = line.strip().split()
            dstport = columns[5]
            protocol_num = columns[7]

            # Map protocol numbers to corresponding protocol names (TCP, UDP, ICMP)
            if protocol_num == '6':
                protocol = 'tcp'
            elif protocol_num == '17':
                protocol = 'udp'
            else:
                protocol = 'icmp'


            # Retrieve the tag for the (dstport, protocol) combination, making sure have default value as 'Untagged' if no match is found
            tag = tag_mapping.get((dstport, protocol), 'Untagged')
            
            # Increment counts for both the tag and the port/protocol combination
            tag_count[tag] += 1
            port_protocol_count[(dstport, protocol)] += 1

    return tag_count, port_protocol_count

# Function to write the output of tag and port/protocol counts to a file
def save_output(output_file, tag_count, port_protocol_count):
    with open(output_file, 'w') as file:
        # Write tag counts
        file.write('Tag Counts:\n')
        file.write('Tag,Count\n')
        for tag, count in tag_count.items():
            file.write(f'{tag},{count}\n')

        # Write port/protocol combination counts
        file.write('\nPort/Protocol Combination Counts:\n')
        file.write('Port,Protocol,Count\n')
        for (port, protocol), count in port_protocol_count.items():
            file.write(f'{port},{protocol},{count}\n')

