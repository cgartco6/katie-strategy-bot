# Katie Strategy Signal Bot

This repository contains an implementation of Katie's Pocket Option strategy using Heikin Ashi 1M candles and a triple Moving Average setup.

## Strategy Indicators
- **SMA 4** (Green)
- **EMA 50** (Red)
- **EMA 200** (White) - Major Trend Filter
- **Stochastic (5,1,1)** - Momentum Confirmation

## Loss Prevention Feature
This bot generates a **PRE-SIGNAL** (Setup) alert when indicators are aligning but haven't crossed yet. This allows the trader to prepare and verify the trend before the **ACTUAL SIGNAL** (Entry) triggers.

## Installation
1. Install Python 3.9+
2. `pip install -r requirements.txt`
3. Update `config.py` with your Telegram credentials.
4. Run `python main.py`.
