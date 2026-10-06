#!/usr/bin/env python3
"""
Raupulus Music — Servidor local de desarrollo
Sirve la carpeta dist/ en http://localhost:8080 y permite previsualizar la web completa
incluyendo los reproductores de YouTube oficiales sin Error 153.
"""
import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        super().end_headers()

def main():
    if not os.path.exists(DIST_DIR):
        print(f"Error: No existe el directorio {DIST_DIR}. Ejecuta 'python3 build.py' primero.")
        sys.exit(1)

    port = PORT
    server = None
    for p in range(PORT, PORT + 20):
        try:
            server = socketserver.TCPServer(("", p), Handler)
            port = p
            break
        except OSError:
            continue

    if not server:
        print("No se pudo iniciar el servidor en el rango de puertos 8080-8100.")
        sys.exit(1)

    url = f"http://localhost:{port}"
    print("=" * 65)
    print(f"  🔥 RAUPULUS MUSIC — Servidor Local de Desarrollo")
    print(f"  🌐 URL Inicio:  {url}")
    print(f"  🎵 Canción 01:  {url}/canciones/01-corona-de-hierro.html")
    print(f"  🛑 Pulsa Ctrl+C para detener el servidor.")
    print("=" * 65)

    if "--no-browser" not in sys.argv:
        try:
            webbrowser.open(url)
        except Exception:
            pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
