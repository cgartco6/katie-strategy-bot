import time
from src.engine import KatieStrategy
from src.telegram_bot import broadcast_signal
from config import MAJOR_PAIRS

def get_mock_market_data(pair):
    """
    In a real scenario, you would replace this with your 
    Broker API or MetaTrader 5 bridge data.
    """
    return {
        'close': 1.0850,
        'sma4': 1.0845,
        'ema50': 1.0855,
        'ema200': 1.0820,
        'stoch_k': 75
    }

def run_bot():
    print("🚀 Katie Strategy Bot Started...")
    
    # Simple loop to check pairs
    while True:
        for pair in MAJOR_PAIRS:
            data = get_mock_market_data(pair)
            status = KatieStrategy.analyze(data)
            
            if status != "NEUTRAL":
                print(f"[{pair}] {status} detected. Sending signal...")
                broadcast_signal(pair, status, data['close'])
            
        # Wait 60 seconds (1-minute candle timeframe)
        time.sleep(60)

if __name__ == "__main__":
    run_bot()
