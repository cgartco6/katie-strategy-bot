class KatieStrategy:
    """
    Implements Katie's Pocket Option strategy with an added 
    pre-signal layer to prevent losses from false breakouts.
    """
    @staticmethod
    def analyze(data):
        """
        data structure: {'close', 'sma4', 'ema50', 'ema200', 'stoch_k'}
        """
        price = data['close']
        sma4 = data['sma4']
        ema50 = data['ema50']
        ema200 = data['ema200']
        stoch = data['stoch_k']

        # --- BUY LOGIC ---
        # 1. Pre-Signal: Price is above long trend, SMA4 is below EMA50 but rising
        if price > ema200 and sma4 < ema50:
            return "PRE-BUY (Setup Forming)"
        
        # 2. Actual Signal: SMA4 crosses above EMA50 + Stochastic confirmation
        if price > ema200 and sma4 >= ema50 and stoch > 70:
            return "BUY NOW"

        # --- SELL LOGIC ---
        # 1. Pre-Signal: Price is below long trend, SMA4 is above EMA50 but falling
        if price < ema200 and sma4 > ema50:
            return "PRE-SELL (Setup Forming)"
            
        # 2. Actual Signal: SMA4 crosses below EMA50 + Stochastic confirmation
        if price < ema200 and sma4 <= ema50 and stoch < 30:
            return "SELL NOW"

        return "NEUTRAL"
