import subprocess
import csv
import os

def open_incognito_tabs(domains):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 

    command = [chrome_path, "--incognito"]
    command.extend(domains)

    try:
        subprocess.Popen(command)
        print("Chrome launched in incognito mode with tabs!")
    except FileNotFoundError:
        print("Chrome executable not found. Make sure Chrome is installed and in your PATH.")

def read_domains_from_txt(file_path):
    with open(file_path, 'r') as f:
        domains = [line.strip() for line in f if line.strip()]
    return domains

def read_domains_from_csv(file_path, column_name):
    domains = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        if column_name not in reader.fieldnames:
            raise ValueError(f"Column '{column_name}' not found in CSV. Available columns: {reader.fieldnames}")
        for row in reader:
            domain = row.get(column_name)
            if domain:
                domains.append(domain.strip())
    return domains

def main():
    file_path = input("Enter the path to the file (txt or csv): ").strip()

    if not os.path.isfile(file_path):
        print("File does not exist. Please check the path.")
        return

    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == ".txt":
        domains = read_domains_from_txt(file_path)
    elif file_ext == ".csv":
        column_name = input("Enter the column name that contains the domains/IPs: ").strip()
        try:
            domains = read_domains_from_csv(file_path, column_name)
        except ValueError as e:
            print(e)
            return
    else:
        print("Unsupported file type. Please provide a .txt or .csv file.")
        return

    if not domains:
        print("No domains/IPs found in the file.")
        return

    open_incognito_tabs(domains)

if __name__ == "__main__":
    main()
