**5-Day Historical Simulation Value-at-Risk Model for Crypto**

Simple, fast Python script that calculates the 95% 5-day VaR for a BTC-heavy crypto portfolio using real historical data from Yahoo Finance.

---

## Portfolio

- **BTC:** 75%  
- **SOL:** 10%  
- **ETH:** 15%  
- **Total Value:** $100,000

---

## Output

**95% 5-Day VaR** — the worst expected loss over the next 5 days with 95% confidence.

---

## Methodology

- Pulls 12 years of daily prices (BTC, SOL, ETH) via `yfinance`
- Computes daily log returns
- Rolls up to 5-day horizon returns
- Historical simulation (no assumptions about distribution)

---

## Use Cases

- Quick risk snapshot for volatile crypto holdings
- Test different asset weights and portfolio sizes
- Backtest risk levels across market regimes
- Support capital allocation and position sizing
