import json, os, re
from pathlib import Path
from urllib.parse import urlparse

event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
issue = event['issue']
body = issue.get('body') or ''

def field(label):
    match = re.search(r'^### ' + re.escape(label) + r'\s*\n+([^\n]+)', body, re.M)
    return match.group(1).strip() if match else ''

reg = field('Register number').upper()
repo = field('GitHub repository').rstrip('/')
if not re.fullmatch(r'26PCA\d{3}', reg):
    raise SystemExit('Invalid register number')
u = urlparse(repo)
if u.scheme != 'https' or u.netloc.lower() != 'github.com' or not re.fullmatch(r'/[A-Za-z0-9-]+/[A-Za-z0-9._-]+', u.path) or u.query or u.fragment:
    raise SystemExit('Invalid GitHub repository URL')
path = Path('submissions.json')
records = json.loads(path.read_text()) if path.exists() else []
records = [r for r in records if r.get('regnumber') != reg]
records.append({'regnumber': reg, 'github_repo': repo})
records.sort(key=lambda r: r['regnumber'])
path.write_text(json.dumps(records, indent=2) + '\n')
print('Saved', reg)
