import requests
import os

def send_signal(pair, action, price, strength):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    message = (
        f"🚨 *KATIE SIGNAL DETECTED*\n\n"
        f"💎 **Pair:** {pair}\n"
        f"📉 **Action:** {action}\n"
        f"🎯 **Entry Price:** {price}\n"
        f"⚡ **Strength:** {strength}\n"
        f"⏰ **Timeframe:** 1 Min\n"
        f"⚠️ *Check candle color before entry!*"
    )
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)
