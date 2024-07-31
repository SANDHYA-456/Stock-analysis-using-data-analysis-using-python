                                              STOCK ANALYSIS WITH DATA ANALYSIS USING PYTHON
          
                                     
                                                          PANDAS



#INTILALIZE THE PANDAS
import pandas as pd

#READ THE DATA SET
data=open("stocks.csv")
print(data.read())

#TO KNOW THE TYPE OF DATA WHETHER STRING OR INT OR FLOAT ETC..
data=open("stocks.csv")
file=data.read()
print(file,type(file))

#WHEN PRINT IS GIVEN WE GET TEXTUAL FORMAT (JUST DISPLAY) WHEN RETURNING WE GET EXACT FORMAT DISPLAYED IN DATA FRAME
print(df)

#THE STRING TO BE IN DATA FRAME
sto=pd.read_csv("stocks.csv")
df=pd.DataFrame(sto)
df

#TO PRINT MAX NUMBER IN DATA SET
df.max()

#TO PRINT MIN NUMBER IN DATA SET
df.min()

#BASIC ANALYSIS
#HEAD METHOD IS USED TO PRINT FEW ROWS FROM THE DATA SET
df.head(7)

#TAIL METHOD PRINT LAST FEW ROWS
df.tail()

#WHILE READING THE FILE WE CAN IGNORE SOME COLUMNS BY USING THIS
#usecols=['Volume']
df.index

#ADDING USER INDEX MANUALLY AS INDEX IS STARTING FROM 0  SO TO START FROM 1
df.index=[v for v in range(1,249)]
df

#TO GET OR RETRIEVE ONLY PARTICULAR COLUMN BY SLICING 
#single[] it will be 1 dimensional(series)
df['Ticker'] 

#df[[]] REPRESENTS IN DATA FRAME
df[['Close']]

df[['Close','High']]

#TO COUNT OR UNDER THIS THE NO OF SAMPLES
df[['Close','High']].count()

df['High'].sum()

#loc and iloc   MANUAL OPERATIONS
df['Total']=df[['High','Low']].sum(axis=1)
df

df.loc[5:30,['Date']] #SPECIFIC SLICING

df.iloc[2,5:] 

df.iloc[5:,1] 

#TEXTUAL INFORMATION
df.info()

df.describe() #GIVES THE STATISTICS

# RESULT THE BOOLEAN DATA FRAME
df.isna()
df.isnull()

#TO FIND COUNT OF ALL NULL VALUES OR FREQUENCY OF NULL DATA 
df.isnull().sum()

df.isna().count() #IT GIVES NO OF RECORDS IN EACH COLUMN

df.High.value_counts()#COUNTS THE FREQUENCY OF DATA ITEMS IN HIGH ALL ARE UNIQUE DATA SO 1 TIME IS THERE 


                                                        
                                                                    MATPLOTLIB


BARGRAPH

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame

stocks_df = pd.read_csv('stocks.csv')

# Convert the 'Date' column to datetime format
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])

# List of unique tickers
tickers = stocks_df['Ticker'].unique()

# Create subplots for each ticker
fig, axs = plt.subplots(len(tickers), 2, figsize=(12, 6 * len(tickers)))

for i, ticker in enumerate(tickers):
    ticker_df = stocks_df[stocks_df['Ticker'] == ticker]
    ticker_df.set_index('Date', inplace=True)
# Plot closing prices
    axs[i, 0].plot(ticker_df.index, ticker_df['Close'], label='Close Price')
    axs[i, 0].set_title(f'{ticker} Closing Prices Over Time')
    axs[i, 0].set_xlabel('Date')
    axs[i, 0].set_ylabel('Closing Price (USD)')
    axs[i, 0].legend()
    axs[i, 0].grid(True)
    
    # Plot trading volume
    axs[i, 1].bar(ticker_df.index, ticker_df['Volume'], color='orange')
    axs[i, 1].set_title(f'{ticker} Trading Volume Over Time')
    axs[i, 1].set_xlabel('Date')
    axs[i, 1].set_ylabel('Volume')
    axs[i, 1].grid(True)

plt.tight_layout()
plt.show()






HISTOGRAM


df.hist(bins=30,figsize=(20,15))
plt.show()



PIE CHART

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
sto=pd.read_csv("stocks.csv")
df=pd.DataFrame(sto)
# Aggregate the volume data by ticker
volume_by_ticker = df.groupby('Ticker')['Volume'].sum()

# Plot the pie chart
plt.figure(figsize=(5, 5))
plt.pie(volume_by_ticker, labels=volume_by_ticker.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Trading Volumes by Ticker')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()