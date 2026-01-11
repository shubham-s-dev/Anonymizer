import random
import os 
import pandas as pd


sensitive_folder = "sensitive_data"
sensitive_data = []
important_ext = [".pdf", ".docx", ".xlsx"]

# Check agar folder exist karta hai
if not os.path.exists(sensitive_folder):
    os.makedirs(sensitive_folder)
    print(f"Created folder '{sensitive_folder}'. Please put some files in it and run again.")
    exit()

files = os.listdir(sensitive_folder)

# --- PHASE 2: THE LOOP ---
for filename in files :
    
    old_path = os.path.join(sensitive_folder, filename)


    if os.path.isfile(old_path):
        
        _, file_ext = os.path.splitext(filename)

        if file_ext in important_ext:

           if filename == "Secret_Map.xlsx":
                continue 
           
           secret_code = random.randint(1000, 9999)

           new_filename = "Candidate_" + str(secret_code) + file_ext

           new_path = os.path.join(sensitive_folder, new_filename)

           os.rename(old_path, new_path)

           sensitive_data.append({
                "Original Name": filename,
                "Hidden Name": new_filename,
                "Code": secret_code
            })
           print(f"Renamed: {filename} -> {new_filename}")
           
# --- PHASE 3: REPORTING ---
if len(sensitive_data) > 0:
    df = pd.DataFrame(sensitive_data)
    excel_path = os.path.join(sensitive_folder, "Secret_Map.xlsx")
    df.to_excel(excel_path, index=False)
    print(f"\nMission Accomplished! Secret Map saved inside '{sensitive_folder}'.")
else:
    print("\nNo matching files found to rename.")