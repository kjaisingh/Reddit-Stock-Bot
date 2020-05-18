# Reddit Stock Bot
A Reddit-based bot that when invoked, provides information including daily highs/lows of a stock, information about the stock's company and recent recommendations on whether to buy or sell the stock. \
The bot operates on the /r/Investing and /r/Stocks subreddits, and is compatible with all stocks on the S&P-500, NASDAQ and NYSE indexes. \
The bot can be found on Reddit as /u/StockInfoBot. 


### Invokation
A sample invokation of the bot in the comments section of a post in one of the above subreddits is as follows:\
*How is the stock of $$AAPL doing?*

The corresponding bot response is:\
*Hello! This is the StockInfoBot. I have come here to provide information about the AAPL stock.*
*Stock Name: Apple Inc.*\
*Day Low: $300.42.*\
*Day High: $307.9.*\
*Trading Volume: 41587094.*\
*50 Day Average: $281.61237.*\
*200 Day Average: $283.89764.*\
*Company Industry: Consumer Electronics.*\
*Company Website*: http://www.apple.com. \
*Recent Analysis by Analysts: Wedbush - Outperform, Raymond James - Outperform, DA Davidson - Buy, Nomura Instinet - Neutral, UBS - Buy.*

### Execution
1. Extract stock ticker information from dataset with S&P-500 information. 
~~~~
python extraction.py
~~~~~~~~ 

2. Execute Reddit bot after replacing information in the client_id, client_secret, username and password fields.
~~~~
python stockinfobot.py
~~~~~~~~ 
