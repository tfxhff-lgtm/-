from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
URL = "http://127.0.0.1:8765/"
ASSET_PREFIXES = ("/assets/", "/api/", "/manus-storage/", "/__manus__/")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        route = unquote(urlsplit(self.path).path)
        target = (ROOT / route.lstrip("/")).resolve()
        if target.is_file() or route == "/":
            return super().do_GET()
        if route.startswith(ASSET_PREFIXES):
            return self.send_error(404, "Asset not found")
        self.path = "/index.html"
        return super().do_GET()

server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
print(f"Sol y Mesa is ready: {URL}\nClose this window to stop the local server.")
threading.Timer(0.8, lambda: webbrowser.open_new_tab(URL)).start()
server.serve_forever()
