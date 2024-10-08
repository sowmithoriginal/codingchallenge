# Codingchallenge

## Assumptions, Functionality
The code is divided into different helper functions for parsing the lookup table, constructing the mapper of (dst port, protocol) to the tag, and one which parses the logs and maps each log to a respective tag based on the lookup values, and finally one function for writing to the output file with the relevant information from the constructed mappers from the functions.

The assumptions include the standard log structure mentioned ( I have gone through the logs in the portal which has a specific structure with relevant data types for each feild), so when there's a slight change in the format of logs, we could integrate the changes in the process_flow_logs helper function seamlessly if needed and the default values for the respective protocols like tcp,udp,icmp are assumed.

## Testing, Results

I have verified the functionality of the code using different test files for the flowlogs.txt as well as lookup.csv, one such instances were uploaded here, the code handlles the requirements such as case_insensitivity, and same tag can have different port, protocol combinations and displays the results in output.txt file

## Steps to run the code

1)Clone the repo using the following command
```
https://github.com/sowmithoriginal/codingchallenge.git

```

2)Run the main.py file

```
python3 main.py
```
