# Codingchallenge

## Assumptions, Functionality
Helper Functions: The code is organized into well-defined helper functions, each performing a specific task:
Parsing the lookup table (CSV file)
Constructing a mapper that links destination port and protocol combinations to tags
Parsing log entries (text file)
Matching each log entry to a tag based on the lookup table data
Writing mapped results to an output file
Flexibility: The code assumes a standard log structure, allowing for seamless integration if the format changes slightly. Modifications would primarily involve the process_flow_logs helper function.
Defaults: Default values are used for common protocols like TCP, UDP, and ICMP.


## Testing, Results

I have verified the functionality of the code using different test files for the flowlogs.txt as well as lookup.csv, one such instances were uploaded here, the code handles the requirements such as case_insensitivity, and same tag can have different port, protocol combinations and displays the results in output.txt file

## Steps to run the code

1)Clone the repo using the following command
```
https://github.com/sowmithoriginal/codingchallenge.git

```

2)Run the main.py file

```
python3 main.py
```
