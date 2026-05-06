import time
import yaml
from dotenv import load_dotenv
from src.indicators import apply_indicators
from src.strategy import check_bearish_signal
from src.telegram_api import send_signal

# Note: You would replace 'get_live_data' with your specific broker's API call
from your_data_provider import get_live_data 

load_dotenv()

with open("config/pairs.yaml", "r") as f:
    config = yaml.safe_load(f)

def run_bot():
    print("🚀 Katie Strategy Monitor Started...")
    while True:
        for pair in config['pairs']:
            # Fetch 1-min data
            df = get_live_data(pair, interval="1m") 
            df = apply_indicators(df)
            
            result = check_bearish_signal(df)
            
            if result:
                send_signal(pair, result['signal'], result['price'], result['strength'])
                print(f"✅ Signal sent for {pair}")
        
        # Poll every 10 seconds to catch signals early within the 1-min candle
        time.sleep(10)

if __name__ == "__main__":
    run_bot()
