# Monero Proxy

Tiny example of a Flask-based backend API acting as a Monero proxy with some business logic.

Start the server
```bash
HOST=127.0.0.1 PORT=8000 python app.py
```


Make a transfer request against the proxy (just an example)
```curL
curl -X POST \
	http://127.0.0.1:8000/transfer \
	-d '{"destinations":["some monero address"],"account_index":0}' \
	-H "Content-Type: application/json;charset=utf8" \
	-H "Accept: application/json;charset=utf8"
```
