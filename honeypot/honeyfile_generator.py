import os

HONEYFILES = [
"passwords.txt",
"bank_details.txt",
"wallet_keys.txt",
"confidential_data.pdf"
]

TARGET_DIRS = [
"test_folder/Documents",
"test_folder/Downloads",
"test_folder/Desktop"
]

def create_honeyfiles():

for directory in TARGET_DIRS:
    os.makedirs(directory, exist_ok=True)

    for filename in HONEYFILES:
        filepath = os.path.join(directory, filename)

        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                file.write("This is a honeyfile for ransomware detection.\n")

print("Honeyfiles generated successfully.")
