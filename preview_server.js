const http = require('http');
const fs = require('fs');
const path = require('path');

// Read the base template once
const baseHtml = fs.readFileSync(path.join(__dirname, 'templates', 'base.html'), 'utf-8');

const server = http.createServer((req, res) => {
    // Simulate successful login/signup for the preview
    if (req.method === 'POST') {
        res.writeHead(302, { 'Location': '/dashboard' });
        res.end();
        return;
    }

    let url = req.url === '/' ? '/login' : req.url;
    
    // Serve static files (CSS/JS)
    if (url.startsWith('/static/')) {
        const filePath = path.join(__dirname, url);
        if (fs.existsSync(filePath)) {
            const ext = path.extname(filePath);
            const contentType = ext === '.css' ? 'text/css' : ext === '.js' ? 'application/javascript' : 'text/plain';
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(fs.readFileSync(filePath));
        } else {
            res.writeHead(404);
            res.end('Static file not found');
        }
        return;
    }

    // Determine the template to render
    let templateName = url.substring(1).split('?')[0].split('/')[0]; // Remove query params and subpaths
    
    // Map /department/... and /company/... to their templates
    if (url.startsWith('/departments')) templateName = 'departments';
    else if (url.startsWith('/department/')) templateName = 'department';
    else if (url.startsWith('/company')) templateName = 'company';
    else if (url.startsWith('/role')) templateName = 'role';

    if (!templateName || templateName === '') templateName = 'login';
    
    const templatePath = path.join(__dirname, 'templates', `${templateName}.html`);
    
    if (fs.existsSync(templatePath)) {
        let contentHtml = fs.readFileSync(templatePath, 'utf-8');
        
        // Extract dynamic content blocks (Basic Regex Parsing for Jinja templates)
        let contentMatch = contentHtml.match(/{%\s*block\s+content\s*%}([\s\S]*?){%\s*endblock\s*%}/);
        let blockContent = contentMatch ? contentMatch[1] : `<h1>Failed to render block</h1><p>${contentHtml}</p>`;

        let titleMatch = contentHtml.match(/{%\s*block\s+title\s*%}([\s\S]*?){%\s*endblock\s*%}/);
        let titleBlock = titleMatch ? titleMatch[1] : 'Placement Prep AI';
        
        // Render into base HTML and clean up Jinja specific tags
        let finalHtml = baseHtml
            .replace(/{%\s*block\s+title\s*%}[\s\S]*?{%\s*endblock\s*%}/, titleBlock)
            .replace(/{%\s*block\s+content\s*%}[\s\S]*?{%\s*endblock\s*%}/, blockContent)
            // Fix static file links
            .replace(/{{.*?url_for\('static',\s*filename='(.*?)'\).*?}}/g, '/static/$1')
            // Fix basic route links so clicking them works in the preview
            .replace(/{{.*?url_for\('([a-zA-Z0-9_]+)'.*?\).*?}}/g, '/$1')
            // Clean up left over {% if %} logic from navbar manually
            .replace(/{% if session.get\('user_id'\) %}[\s\S]*?{% else %}/, '')
            .replace(/{% endif %}/g, '')
            // Clean up left over syntax variables
            .replace(/{{.*?username.*?}}/g, 'Student')
            .replace(/{{.*?dept.*?}}/g, 'ECE')
            .replace(/{{.*?company.name.*?}}/g, 'NVIDIA')
            .replace(/{{.*?company.domain.*?}}/g, 'Semiconductor/AI')
            .replace(/{{.*?company.profile.*?}}/g, 'Leader in GPU-accelerated computing, artificial intelligence, and semiconductor design.')
            .replace(/{{.*?role.name.*?}}/g, 'VLSI Design Engineer')
            .replace(/{%.*?%}/g, '');

        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(finalHtml);
    } else {
        res.writeHead(404);
        res.end(`<h1>404 Not Found (${templatePath})</h1><a href="/login">Go to Login preview</a>`);
    }
});

server.listen(8000, () => {
    console.log('----------------------------------------------------');
    console.log('  UI PREVIEW SERVER RUNNING');
    console.log('  View the website at: http://localhost:8000');
    console.log('----------------------------------------------------');
});
