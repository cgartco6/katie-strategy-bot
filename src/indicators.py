import pandas_ta as ta

def apply_indicators(df):
    # EMA 10 (Blue) and EMA 3 (Yellow)
    df['ema_10'] = ta.ema(df['close'], length=10)
    df['ema_3'] = ta.ema(df['close'], length=3)
    
    # MACD (15, 27, 9)
    macd = ta.macd(df['close'], fast=15, slow=27, signal=9)
    df['macd_hist'] = macd['MACDh_15_27_9']
    
    # Vortex (10)
    vortex = ta.vortex(df['high'], df['low'], df['close'], length=10)
    df['v_plus'] = vortex['VTXP_10']
    df['v_minus'] = vortex['VTXM_10']
    
    return df
