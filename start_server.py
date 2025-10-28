#!/usr/bin/env python3
"""
Simple HTTP Server for Color Changer Tool
Fixes CORS issues when loading local images
"""

import http.server
import socketserver
import webbrowser
import os
import sys

# Change to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        # Handle preflight CORS requests
        self.send_response(200)
        self.end_headers()

def start_server():
    """Start the HTTP server and open the browser"""
    try:
        with socketserver.TCPServer(("", PORT), CORSHTTPRequestHandler) as httpd:
            server_url = f"http://localhost:{PORT}"
            app_url = f"{server_url}/advanced-color-changer.html"
            
            print(f"🚀 Starting server at {server_url}")
            print(f"📂 Serving files from: {os.getcwd()}")
            print(f"🌐 Opening Color Changer at: {app_url}")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Open the browser automatically
            webbrowser.open(app_url)
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 10048:  # Address already in use on Windows
            print(f"❌ Port {PORT} is already in use!")
            print(f"💡 Try opening http://localhost:{PORT}/advanced-color-changer.html in your browser")
            print(f"💡 Or change the PORT number in this script")
        else:
            print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🎨 Color Changer Tool - HTTP Server")
    print("=" * 50)
    start_server()