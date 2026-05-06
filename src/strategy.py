def check_bearish_signal(df):
    """
    Implements Katie's Bearish Rule:
    1. EMA 3 < EMA 10
    2. Vortex Minus > Vortex Plus
    3. MACD Hist < 0 (Ideally first 4 bars)
    4. Price Candle is Red
    """
    row = df.iloc[-1]
    prev_row = df.iloc[-2]
    
    # EMA Condition
    ema_condition = row['ema_3'] < row['ema_10']
    
    # Vortex Condition
    vortex_condition = row['v_minus'] > row['v_plus']
    
    # MACD Condition (Freshness check)
    is_bearish_hist = row['macd_hist'] < 0
    fresh_macd = (df['macd_hist'].iloc[-5] > 0) # Cross happened within last 4 candles
    
    # Price Action (Red Candle)
    is_red = row['close'] < row['open']

    if ema_condition and vortex_condition and is_bearish_hist and is_red:
        strength = "HIGH" if fresh_macd else "MODERATE"
        return {
            "signal": "SELL",
            "strength": strength,
            "price": row['close']
        }
    return None
