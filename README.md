# URL Shortener

#### Flask TinyURL clone.

```python
# API requests
import requests

address = "<your server IP here>"
payload = {
    "shortened": "github",
    "url": "https://www.github.com"
}

r = requests.post(address + "/create", json=payload)
print(r.text)
```

```markdown
# redirects
http://address/github -> https://www.github.com
```
