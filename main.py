
from logparser import load_tag_mappings, process_flow_logs, save_output


# Main function to load data, process logs, and write output
def main(lookup_file, flow_file, output_file):
    tag_mapping = load_tag_mappings(lookup_file)
    tag_count, port_protocol_count = process_flow_logs(flow_file, tag_mapping)
    save_output(output_file, tag_count, port_protocol_count)

if __name__ == "__main__":
    lookup_file = 'lookup.csv'       # Path to the lookup table CSV file
    flow_file = 'flowlogs.txt'       # Path to the flow logs file
    output_file = 'output.txt'       # Path to the output file

    main(lookup_file, flow_file, output_file)
