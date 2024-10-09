# Coding Challenge

## Project Overview

This Python script is designed to process log entries and assign tags based on a provided lookup table. It efficiently maps destination port and protocol combinations to corresponding tags, ensuring accurate categorization.

## Functionality

* **Lookup Table Parsing:** Reads a CSV file containing lookup table data, mapping destination ports and protocols to tags.
* **Mapper Construction:** Creates a dictionary-based mapper that associates destination port-protocol combinations with their respective tags.
* **Log Entry Parsing:** Processes log entries from a text file, extracting relevant information like destination port, protocol, and timestamp.
* **Tag Matching:** Matches parsed log entries to tags using the constructed mapper.
* **Output Generation:** Writes the matched log entries and their corresponding tags to an output file (`output.txt`).

## Assumptions and Flexibility

* **Log Structure:** Assumes a standard log format, allowing for easy adaptation to minor changes.(I have gone through the portal which has a definite structure for logs with feilds and their data types, so any changes in the format of logs, could be seamlessly integrated with the help of process_flow_logs function)
* **Default Protocols:** Uses default values for common protocols (TCP, UDP, ICMP).

## Testing and Verification

Rigorous testing has been conducted using various test files to ensure:

* Correct tag assignment for different port-protocol combinations.
* Handling of case-insensitivity.
* Proper output generation.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sowmithoriginal/codingchallenge.git
2. **Navigate to the directory and run main.py:**

   ```bash
   python3 main.py
