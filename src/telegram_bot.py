import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def broadcast_signal(pair, status, price):
    """Sends formatted signal to Telegram."""
    
    # Visual cues for status
    if "PRE" in status:
        icon = "🟡"
        header = "PRE-SIGNAL (WATCHING)"
    else:
        icon = "🟢" if "BUY" in status else "🔴"
        header = "ACTUAL SIGNAL (ENTRY)"

    message = (
        f"{icon} *{header}* {icon}\n\n"
        f"💹 *Pair:* {pair}\n"
        f"📢 *Action:* {status}\n"
        f"💵 *Price:* {price}\n\n"
        f"🕒 *Timeframe:* 1M\n"
        f"⚠️ *Note:* No stop-loss active (Katie Style)"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID, 
        "text": message, 
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, data=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Telegram Error: {e}")
        return False
