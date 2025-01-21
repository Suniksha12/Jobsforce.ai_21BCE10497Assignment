import sys
import json
import pdfplumber
import spacy
import re

def extract_phone_number(text):
    # Pattern for phone numbers (adjust as needed)
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    matches = re.findall(phone_pattern, text)
    return matches[0] if matches else None

def extract_information(pdf_path):
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")
    
    extracted_info = {
        "name": None,
        "phone": None,
        "address": None
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

        # Extract phone number
        extracted_info["phone"] = extract_phone_number(text)

        # Process text with spaCy
        doc = nlp(text)

        # Extract name (looking for PERSON entities)
        for ent in doc.ents:
            if ent.label_ == "PERSON" and not extracted_info["name"]:
                extracted_info["name"] = ent.text

        # Extract address (looking for multiple lines with location indicators)
        address_indicators = ["street", "avenue", "road", "boulevard", "lane"]
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if any(indicator in line_lower for indicator in address_indicators):
                # Take current line and next line as address
                extracted_info["address"] = " ".join([lines[i], lines[i+1]]).strip()
                break

        print(json.dumps(extracted_info))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "PDF path not provided"}))
        sys.exit(1)
    
    extract_information(sys.argv[1])