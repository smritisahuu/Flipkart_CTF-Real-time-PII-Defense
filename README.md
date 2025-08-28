# 🔒 PII Redaction Solution

This project detects and masks **Personally Identifiable Information (PII)** from CSV records.  
The solution uses regex patterns and masking functions to protect sensitive fields like:

- Phone numbers  
- Aadhaar numbers  
- Passport numbers  
- UPI IDs  
- Email addresses  
- Names & Addresses  

---

## 📂 Files in this Repository
- `detector_full_candidate_name.py` → Main Python script for detecting and masking PII.  
- `iscp_pii_dataset.csv` → Input dataset (sample records provided for testing).  
- `redacted_output_candidate_full_name.csv` → Output dataset (with PII redacted).  
- `deployment_proposal.md` → Deployment strategy (Browser Extension model).  
- `README.md` → Project guide (this file).  

---

## ▶️ How to Run
Run the script with:

```bash
python3 detector_full_candidate_name.py iscp_pii_dataset.csv
