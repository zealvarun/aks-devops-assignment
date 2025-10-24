# scripts/grafana-export-report.py
import requests
import csv
from datetime import datetime, timedelta


PROM_URL = "http://<PROMETHEUS_HOST>/api/v1/query_range"


queries = {
'cpu_usage': 'sum(rate(container_cpu_usage_seconds_total{namespace="sample-app"}[5m])) by (pod)',
'mem_usage': 'sum(container_memory_usage_bytes{namespace="sample-app"}) by (pod)',
'http_errors': 'sum(rate(http_requests_total{code=~"5..", namespace="sample-app"}[5m]))',
'http_lat_p95': 'histogram_quantile(0.95, sum(rate(http_request_duration_ms_bucket{namespace="sample-app"}[5m])) by (le))'
}


end = datetime.utcnow()
start = end - timedelta(days=1)
step = '60s'


rows = []
for name, q in queries.items():
resp = requests.get(PROM_URL, params={'query': q, 'start': start.isoformat()+'Z', 'end': end.isoformat()+'Z', 'step': step})
data = resp.json()
rows.append((name, data))


# Very simple dump
with open('daily_report.json','w') as f:
import json
json.dump({k:v for k,v in rows}, f, indent=2)


print('Report generated: daily_report.json')