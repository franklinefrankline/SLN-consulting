# -*- coding: utf-8 -*-
"""
SLN Consulting Local Development Server
"""
import http.server
import socketserver
import os
import sys

PORT = 5500
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.html': 'text/html',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml',
    '.webp': 'image/webp'
})

print("=" * 60)
print("  SLN CONSULTING — LOCAL DEVELOPMENT SERVER")
print("=" * 60)
print(f"  > Website Home:        http://localhost:{PORT}/")
print(f"  > Internship Redesign: http://localhost:{PORT}/internships.html")
print(f"  > Stop Server:         Press Ctrl + C")
print("=" * 60)

socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer gracefully stopped.")
    sys.exit(0)
