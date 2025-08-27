import time, json, pathlib

def record_run(service_name, status, rows=None, duration_s=None, metrics=None):
    """Append a single run event to an ndjson file for later aggregation."""
    payload = {
        "service": service_name,
        "status": status,
        "rows": rows,
        "duration_s": duration_s,
        "metrics": metrics or {},
        "ts": int(time.time())
    }
    p = pathlib.Path("build/telemetry.ndjson")
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as f:
        f.write(json.dumps(payload) + "\n")
