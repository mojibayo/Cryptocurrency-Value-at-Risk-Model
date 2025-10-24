# Crypto Portfolio VaR Model

> *This Python script calculates the 5-day Value at Risk (VaR) for a cryptocurrency portfolio using historical price data from Yahoo Finance. The assets in the portfolio include Bitcoin (BTC), Solana (SOL), and Ethereum (ETH).*

## Portfolio Allocation

- **BTC:** `75%`
- **SOL:** `10%`
- **ETH:** `15%`
- **Portfolio Value:** `$100,000`

## Methodology

- Fetches 12 years of daily historical data
- Computes log returns for each asset
- Aggregates rolling 5-day returns
- Uses historical simulation to estimate the 95% VaR

## Value at Risk (VaR)

> *The model calculates the worst-case expected loss over the next 5 days with 95% confidence.*

## Requirements

- Python 3.x
- pandas
- numpy
- yfinance
- colorama

## Use Cases

1. **Portfolio Risk Management:** Understand short-term risk in volatile crypto assets.
2. **Capital Allocation:** Adjust asset weights based on acceptable downside.
3. **Backtesting:** Compare different portfolio compositions over historical market behavior.

##

`Might add inputs for more flexibility and better UX.`
- vythea ✷
