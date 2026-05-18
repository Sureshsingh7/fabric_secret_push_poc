import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from sample_app import secrets_fixture


class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._write_json({"status": "ok"}, 200)
            return

        if self.path == "/demo-secrets":
            payload = {
                "message": "Demo-only fake secrets for scanning tests",
                "github_pat": secrets_fixture.GITHUB_PAT,
                "aws_secret_access_key": secrets_fixture.AWS_SECRET_ACCESS_KEY,
                "aws_access_key_id": secrets_fixture.AWS_ACCESS_KEY_ID,
                "slack_bot_token": secrets_fixture.SLACK_BOT_TOKEN,
                "azure_storage_connection_string": secrets_fixture.AZURE_STORAGE_CONNECTION_STRING,
            }
            self._write_json(payload, 200)
            return

        self._write_json({"error": "not found"}, 404)

    def log_message(self, fmt, *args):
        return

    def _write_json(self, payload, code):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run(port=8080):
    server = HTTPServer(("127.0.0.1", port), DemoHandler)
    print(f"Sample app listening on http://127.0.0.1:{port}")
    print("Try endpoints: /health and /demo-secrets")
    server.serve_forever()


if __name__ == "__main__":
    run()
