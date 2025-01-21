# Jobsforce.ai_21BCE10497Assignment

# PDF Data Extractor

This project automatically extracts personal information from PDF documents and populates a web form. It uses React for the frontend, Node.js for the backend, and leverages AI models for accurate data extraction.

## Features
- PDF file upload and processing
- Automatic extraction of personal information (Name, Phone, Address)
- Real-time form population with extracted data
- Simple and intuitive user interface

## Prerequisites
- Node.js v16 or higher
- Python 3.8 or higher (for PDF processing)
- npm or yarn package manager

## Installation

### Backend Setup
```bash
cd backend
npm install
pip install -r requirements.txt
npm start
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Technology Stack
- Frontend: React, Axios, TailwindCSS
- Backend: Node.js, Express
- PDF Processing: pdfplumber
- AI/ML: spaCy for NER (Named Entity Recognition)

## Usage
1. Start both frontend and backend servers
2. Navigate to http://localhost:3000
3. Upload a PDF file containing personal information
4. Watch as the form automatically populates with extracted data

## API Endpoints
- POST /api/extract - Accepts PDF file and returns extracted information

## Environment Variables
Create a .env file in the backend directory:
```
PORT=5000
NODE_ENV=development
```
