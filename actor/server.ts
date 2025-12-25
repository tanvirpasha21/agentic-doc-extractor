import express, { Request, Response } from 'express';
import multer from 'multer';
import { spawn } from 'child_process';
import path from 'path';

const upload = multer({ dest: '/tmp/' });
const app = express();

app.post('/extract', upload.single('file'), async (req: Request, res: Response) => {
    if (!req.file) return res.status(400).json({ error: 'No file uploaded' });

    const extractorPath = path.resolve(__dirname, '../worker/extractor.py');
    const filePath = req.file.path;

    const py = spawn('python3', [extractorPath, filePath]);

    let output = '';
    let error = '';

    py.stdout.on('data', (data) => { output += data.toString(); });
    py.stderr.on('data', (data) => { error += data.toString(); });

    py.on('close', (code) => {
        if (error || code !== 0) {
            console.error('Python error:', error);
            return res.status(500).json({ error });
        }
        try { res.json(JSON.parse(output)); }
        catch (e) { res.status(500).json({ error: 'Invalid JSON from Python worker' }); }
    });
});

app.listen(3000, () => {
    console.log('Agentic Document Extractor running on port 3000');
});
