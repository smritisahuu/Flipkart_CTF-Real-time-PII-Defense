import csv  # read/write CSV files
import json # handle JSON strings inside the CSV
import re   #use regular expressions

#Defining regex patterns
PHONE_REGEX= re.compile(r'^\d{10}$')
AADHAAR_REGEX = re.compile(r'^\d{12}$|^(\d{4}\s\d{4}\s\d{4})$')
PASSPORT_REGEX = re.compile(r'^[A-Z]{1,2}[0-9]{6,7}$')
UPI_REGEX = re.compile(r'^[\w\.\-]+@[a-zA-Z]{2,}$')
EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
IP_REGEX = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')


def mask_phone(number):
    return number[:3] + "XXXXXX" + number[-2:]

def mask_aadhaar(aadhar):
    return "XXXXXXXX" + aadhar[-4:]

def mask_passport(passport):
    return passport[0] + "XXXXXX" + passport[-3]

def mask_email(email):
    parts = email.split("@")
    return parts[0][:3] + "XXX@" + parts[1]

def mask_name(name):
    parts = name.split()
    return " ".join([p[0] + "XXX" for p in parts])

# make all keys lowercase
def process_record(record):
    record = {k.lower(): v for k, v in record.items()}
# for skipping the row where no column of data_json
    if "data_json" not in record:
        print(f"[!] Skipping record, no data_json found: {record}")
        return {
            "record_id": record.get("record_id", "NA"),
            "redacted_data_json": "{}",
            "is_pii": False
        }
#converting JSON string from CSV into dictionary
    try:
        data = json.loads(record["data_json"])   # convert JSON string into dict
    except Exception as e:
        print(f"[!] JSON error in record {record.get('record_id','NA')}: {e}")
        return {
            "record_id": record.get("record_id", "NA"),
            "redacted_data_json": "{}",
            "is_pii": False
        }

    is_pii = False  #flag to check if personal info found
    redacted = dict(data)
    combinatorial = {}  # combinatorial PII
   
#looping each field
    for key, value in data.items():
        if not isinstance(value, str) or not value.strip():
            continue

    
        if PHONE_REGEX.fullmatch(value):
            redacted[key] = mask_phone(value)
            is_pii = True
        elif AADHAAR_REGEX.fullmatch(value.replace(" ", "")):
            redacted[key] = mask_aadhaar(value.replace(" ", ""))
            is_pii = True
        elif PASSPORT_REGEX.fullmatch(value):
            redacted[key] = mask_passport(value)
            is_pii = True
        elif UPI_REGEX.fullmatch(value):
            redacted[key] = "[REDACTED_UPI]"
            is_pii = True

        # Combinatorial PII 
        elif key == "name" and len(value.split()) >= 2:
            combinatorial["name"] = mask_name(value)
        elif EMAIL_REGEX.fullmatch(value):
            combinatorial["email"] = mask_email(value)
        elif key == "address":
            combinatorial["address"] = "[REDACTED_ADDRESS]"
        elif key in ("ip_address", "device_id") and value:
            combinatorial[key] = "[REDACTED_" + key.upper() + "]"

    # If at  least 2 combinatorial PII values are present, redacting them
    if len(combinatorial) >= 2:
        is_pii = True
        for k, v in combinatorial.items():
            redacted[k] = v
#Return Result
    return {
        "record_id": record.get("record_id", "NA"),
        "redacted_data_json": json.dumps(redacted),
        "is_pii": is_pii
    }

# For the output
def main(input_file):
    output_file = "redacted_output_candidate_full_name.csv"

    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["record_id", "redacted_data_json", "is_pii"])
        writer.writeheader()

        for row in reader:
            result = process_record(row)
            writer.writerow(result)

    print(f"✅ Done! Output saved to {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 detector_full_candidate_name.py <input_csv>")
    else:
        main(sys.argv[1])
