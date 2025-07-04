# 📄 Day 4 – Azure Document Intelligence (Prebuilt Receipts)

Today I explored a new topic outside of core Python:  
I used Azure AI Document Intelligence Studio to analyze and extract data from receipt images.

## 🔍 What I did:
- Created a new Azure Document Intelligence resource.
- Uploaded a sample receipt image.
- Used a prebuilt model to extract merchant name, date, items, and total.
- Generated Python code to parse receipt data.

## 📦 Technologies:
- Azure Document Intelligence SDK (prebuilt model)
- Python 3.8+
- OCR and key-value extraction

## 📁 Output:
The model parsed structured data from a scanned receipt image and returned fields with confidence scores.

## 📝 Notes:
This exercise is based on the official Microsoft Learn path:  
[Quickstart: Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api)