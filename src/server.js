const express = require('express');
const multer = require('multer');
const cors = require('cors');
const pdfParse = require('pdf-parse');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors({
    origin: process.env.CORS_ORIGIN || '*'
}));
app.use(express.json());

// Test route
app.get('/', (req, res) => {
    res.json({ message: 'PDF Extractor API is running' });
});

app.post('/api/extract', upload.single('pdf'), async (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'No PDF file uploaded' });
    }

    try {
        const dataBuffer = fs.readFileSync(req.file.path);
        const data = await pdfParse(dataBuffer);
        
        // Basic extraction logic
        const text = data.text;
        const extractedData = {
            name: text.slice(0, 50), // Simplified extraction
            phone: text.match(/\d{10}/) ? text.match(/\d{10}/)[0] : '',
            address: text.slice(51, 150)
        };

        // Clean up uploaded file
        fs.unlinkSync(req.file.path);
        
        res.json(extractedData);
    } catch (error) {
        console.error('Error processing PDF:', error);
        res.status(500).json({ error: error.message });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});