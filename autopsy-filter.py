import sys, json, subprocess

ALLOWED = {"get_server_status", "get_case_info", "query_data_artifacts"}
EXE = r"C:\Program Files\Autopsy-4.23.1\bin\autopsy-mcp-stdio.exe"

proc = subprocess.Popen([EXE], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)

def forward_in():
    for line in sys.stdin:
        proc.stdin.write(line)
        proc.stdin.flush()

import threading
threading.Thread(target=forward_in, daemon=True).start()

for line in proc.stdout:
    try:
        msg = json.loads(line)
        if "result" in msg and "tools" in msg["result"]:
            msg["result"]["tools"] = [t for t in msg["result"]["tools"] if t.get("name") in ALLOWED]
            line = json.dumps(msg) + "\n"
    except Exception:
        pass
    sys.stdout.write(line)
    sys.stdout.flush()
