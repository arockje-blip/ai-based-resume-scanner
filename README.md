# AI Hiring Portal - Standalone Website

This is a fully functional website that works **without any backend servers**.

## Quick Start

### Option 1: Open Directly in Browser (No server needed)
Simply open `index.html` in your browser:
- Windows: Double-click `index.html`
- Mac/Linux: Right-click → Open With → Browser
- Or drag `index.html` into your browser window

The entire website will work locally with no server required.

### Option 2: Run a Local Server (For Multiple Devices)
This lets other devices on your network access the website.

**Windows (PowerShell):**
```powershell
python simple_server.py
```

**Mac/Linux:**
```bash
python3 simple_server.py
```

The server will show:
- **Your laptop:** `http://localhost:8000`
- **Other devices:** `http://192.168.x.x:8000` (shown in terminal)

Copy the "Other devices" URL and open it on your phone, tablet, or another computer.

## Website Structure

```
a:\vscode\
├── portal_index.html           # Main landing page (start here)
├── employer_prototype.html    # Employer bulk screening (demo)
├── job_seeker_prototype.html  # Job seeker resume analysis (demo)
├── simple_server.py           # Local HTTP server script
└── README.md                  # This file
```

## Features

### Portal Landing Page
- Clean, simple UI
- Two buttons: Employer and Job Seeker
- All navigation works with relative links

### Employer Portal (Prototype)
- Input: Number of resumes (1-1000) and job description
- Output: Simulated bulk screening results
- No backend server required
- Fully functional in browser

### Job Seeker Portal (Prototype)
- Input: Resume filename and job description
- Output: Simulated ATS match score + improvement tips
- No backend server required
- Fully functional in browser

## How It Works

- **No Backend Calls**: Everything runs in your browser (JavaScript only)
- **No Python Required**: Can be opened as static HTML files
- **Works Offline**: Complete local operation, no internet needed
- **Responsive Design**: Works on desktop and mobile

## Navigation

- From **portal_index.html**: Click buttons to enter Employer or Job Seeker portals
- From **prototypes**: Click "Back to role selection" to return to landing page
- Browser back button also works

## Customization

All files are plain HTML/CSS/JavaScript - feel free to edit:
- Colors in the `<style>` sections
- Text content in the `<body>` elements
- Simulate different data by modifying the JavaScript logic

## Troubleshooting

**Links not working?**
- Make sure all HTML files are in the same folder
- If opening with `file://`, some features may be limited - use `simple_server.py` instead

**Server won't start?**
- Port 8000 may be in use
- Try: `python simple_server.py --port 9000` (requires modifying simple_server.py)
- Or close other applications using the port

**Nothing appears?**
- Refresh the page (F5 or Cmd+R)
- Clear browser cache if you've visited before
- Use a modern browser (Chrome, Firefox, Safari, Edge)

## Deployment Options

To share this with others:

1. **Local Network**: Run `simple_server.py` and share the local IP (e.g., `192.168.1.100:8000`)
2. **Cloud Hosting**: Upload files to GitHub Pages, Netlify, or Vercel (all free)
3. **Static Host**: Works on any web hosting service

## License

This is a prototype demonstration of an AI hiring platform.
