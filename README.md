
# YARH (Yet Another RAM Hunter)


## Overview

This Python script allows investigators, analysts, and researchers to **quickly open multiple domains or IP addresses** in an **incognito Chrome window**, each in a **separate tab**.

It supports input from:
- `.txt` files (one domain/IP per line)
- `.csv` files (user specifies the column containing the domains/IPs)

This is useful when you need to manually inspect multiple domains, such as during **threat investigations**, **domain reputation analysis**, or **incident response** activities.


## Features

- **TXT Support**: Reads domains/IPs line-by-line.
- **CSV Support**: Lets the user specify the desired column containing the domains/IPs.
- **Chrome Incognito Mode**: Ensures browsing is clean and avoids caching, cookies, or login sessions.
- **Batch Opening**: All domains are opened at once in separate tabs.



## Usage

1. Run the script:
    ```bash
    python launch_tabs.py
    ```

2. Input the file path when prompted:
    - Example: `C:\Users\[yourname]\Desktop\domains.txt`
    - Or: `/home/yourname/documents/domains.csv`

3. If it's a **CSV file**, specify the column name that contains the domains or IP addresses when asked.

4. Chrome will open in **Incognito Mode**, launching a new tab for each domain/IP.


## Example Use Cases

- **Incident Response**: Quickly review malicious or suspicious domains gathered from logs or threat intelligence feeds.
- **Threat Hunting**: Open multiple IoCs (Indicators of Compromise) for manual validation.


## Notes

- The script assumes that each domain or IP is a valid URL. 
- If a very large number of tabs are opened at once, Chrome may slow down depending on your system resources.


## Disclaimer

Always be cautious when visiting unknown domains, even in Incognito Mode.  
Consider using a secure environment (like a VM or sandbox) for potentially malicious URLs.

