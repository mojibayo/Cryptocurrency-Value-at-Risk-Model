import numpy      as np
import pandas     as pd
import datetime   as dt
import os
import time
import yfinance   as yf
import math
import colorama

from   colorama     import Fore

error = (f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} ")
info  = (f"{Fore.BLUE}[{Fore.RESET}>{Fore.BLUE}]{Fore.RESET} ")
ldata = (f"{Fore.MAGENTA}[{Fore.RESET}~{Fore.MAGENTA}]{Fore.RESET} ")

years      = 12
endDate    = dt.datetime.now()
startDate  = endDate - dt.timedelta(days=365 * years)

print(f"{ldata} Range: {years} Years || Start Date: {startDate} || End Date: {endDate}")
time.sleep(5)

pairs = ['BTC-USD', 'SOL-USD', 'ETH-USD']

close = pd.DataFrame()
for pair in pairs:
    data = yf.download(pair, start=startDate, end=endDate)
    if 'Close' in data:
        close[pair] = data['Close']
    else:
        print(f"Warning: No Close data for {pair}")

os.system("clear")
print(f"{info}Calculating value at risk on portfolio...")
time.sleep(5)

log_returns = np.log(close/close.shift(1))
log_returns = log_returns.dropna()

portfolio_value  = 100000
weights          = np.array([0.75, 0.1, 0.15])
print(f"\n{info}Pairs Used in Model: BTC-USD, SOL-USD, ETH-USD")
print(f"{ldata}Weight/Portfolio Allocation: {weights[0]*100}% {pairs[0]} || {weights[1]*100}% {pairs[1]} || {weights[2]*100}% {pairs[2]}")

historical_returns  = (log_returns * weights).sum(axis=1)

days                = 5
range_returns       = historical_returns.rolling(window = days).sum()
range_returns       = range_returns.dropna().to_numpy()

confidence_interval = 0.95

vaR   = -np.percentile(range_returns, 100 - (confidence_interval * 100))*portfolio_value
vaR   = math.ceil(vaR)
print(f"\n{ldata}Value at Risk: ${vaR}")
print(f"{info}There is a {confidence_interval*100}% chance that the portfolio will not lose more than ${vaR} in the next {days} days.")
