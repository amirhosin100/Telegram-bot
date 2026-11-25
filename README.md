# AMIR BOT
My personal Telegram bot.

### Dependeices
1. python
2. uv

#### if you don't have uv install it
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Environment variables
- TELEGRAM_TOKEN (Your Telegram token)

### Run
```bash
uv sync --locked
source .venv/bin/activate
python ./src/main.py
```
