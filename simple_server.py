#!/usr/bin/env python3
"""
Simple local HTTP server for the AI Hiring Portal
Accessible from all devices on the local network
Run this script to serve the website
"""
import http.server
import socketserver
import os
import socket
import webbrowser
from pathlib import Path

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

# Change to the directory containing this script
os.chdir(Path(__file__).parent)

# Get local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

try:
    local_ip = get_local_ip()
    
    # Listen on all network interfaces
    with socketserver.TCPServer(("0.0.0.0", PORT), HANDLER) as httpd:
        localhost_url = f"http://localhost:{PORT}"
        network_url = f"http://{local_ip}:{PORT}"
        
        print(f"\n✓ Server started successfully!\n")
        print(f"  Local device:  {localhost_url}")
        print(f"  Other devices: {network_url}")
        print(f"\n  To access from other devices, use: {network_url}")
        print(f"  Press Ctrl+C to stop\n")
        
        try:
            webbrowser.open(localhost_url)
        except:
            pass
        
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n✓ Server stopped")
except OSError as e:
    print(f"✗ Error: {e}")
    print(f"  Port {PORT} may already be in use.")
