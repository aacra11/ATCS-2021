# import statements
import pandas as pd
from matplotlib import pyplot as plt

# importing data
bat_raw = pd.read_csv('BAT-USD.csv')
btc_raw = pd.read_csv('BTC-USD.csv')
doge_raw = pd.read_csv('DOGE-USD.csv')
eth_raw = pd.read_csv('ETH-USD.csv')
musk_raw = pd.read_csv('MUSK-TWT.csv')
dj_raw = pd.read_csv('DOWJONES.csv')

# cleaning data (removing unnecessary columns, selecting dates of interest)
bat_data = bat_raw.drop('Low',axis=1).drop('Market Cap',axis=1)
bat_data = bat_data.iloc[::-1]
bat_data = bat_data.add_prefix('BAT ')

index1 = btc_raw.loc[btc_raw['Date'] == '2020-06-01'].index[0]
index2 = btc_raw.loc[btc_raw['Date'] == '2021-06-01'].index[0]
btc_data = btc_raw.iloc[index1:index2+1].drop('Adj Close',axis=1).drop('Low',axis=1)
btc_data = btc_data.add_prefix('BTC ')

index3 = doge_raw.loc[doge_raw['Date'] == '2020-06-01'].index[0]
index4 = doge_raw.loc[doge_raw['Date'] == '2021-06-01'].index[0]
doge_data = doge_raw.iloc[index3:index4+1].drop('Low',axis=1)
doge_data = doge_data.add_prefix('DOGE ')

index5 = eth_raw.loc[eth_raw['Date'] == '2020-06-01'].index[0]
index6 = eth_raw.loc[eth_raw['Date'] == '2021-06-01'].index[0]
eth_data = eth_raw.iloc[index5:index6+1].drop('Adj Close',axis=1).drop('Low',axis=1)
eth_data = eth_data.add_prefix('ETH ')

index7 = dj_raw.loc[dj_raw['Date'] == '2021-06-01'].index[0]
index8 = dj_raw.loc[dj_raw['Date'] == '2020-06-01'].index[0]
dj_raw = dj_raw.iloc[index7:index8+1]
dj_raw = dj_raw[['Date', 'Change %']].iloc[::-1]
dj_data=pd.DataFrame(columns=['Date','DJ Change'])
dj_data['Date'] = dj_raw['Date']
changes = []
for x in dj_raw['Change %']:
    if float(x[0:len(x)-2]) < 0:
        changes.append("decrease")
    elif float(x[0:len(x)-2]) > 0:
        changes.append("increase")
    else:
        changes.append("equal")
dj_data['DJ Change'] = changes
dj_data = dj_data.reset_index().drop('index', axis=1)

musk_data = musk_raw.iloc[::-1]

# combining data
df = pd.merge(bat_data, btc_data, how="inner", left_on="BAT Date", right_on="BTC Date")
df = pd.merge(df, doge_data, how="inner", left_on="BAT Date", right_on="DOGE Date")
df = pd.merge(df, eth_data, how="inner", left_on="BAT Date", right_on="ETH Date")
df = pd.merge(df, musk_data, how="inner", left_on="BAT Date", right_on="Date")
df = df.drop("BTC Date", axis=1).drop("DOGE Date", axis=1).drop("ETH Date", axis=1).drop("Date", axis=1)
df = pd.merge(df, dj_data, how="outer", left_on="BAT Date", right_on="Date").drop("Date", axis=1)
df = df.rename(columns = {'BAT Date':'Date'})

# broad comparisons of bitcoin price changes with other coins' price changes
plt.plot(df['Date'],df['BAT Open']/df['BAT Open'][0], color='Blue') # plotting price relative to initial price
plt.plot(df['Date'],df['BTC Open']/df['BTC Open'][0], color='Orange')
plt.show()

plt.plot(df['Date'],df['ETH Open']/df['ETH Open'][0], color='Blue')
plt.plot(df['Date'],df['BTC Open']/df['BTC Open'][0], color='Orange')
plt.show()

plt.plot(df['Date'],df['DOGE Open']/df['DOGE Open'][0], color='Blue')
plt.plot(df['Date'],df['BTC Open']/df['BTC Open'][0], color='Orange')
plt.show()

# broad comparisons of bitcoin volume changes with other coins' volume changes
plt.plot(df['Date'],df['BAT Volume']/df['BAT Volume'][0], color='Blue') # plotting volume relative to initial volume
plt.plot(df['Date'],df['BTC Volume']/df['BTC Volume'][0], color='Orange')
plt.show()

plt.plot(df['Date'],df['ETH Volume']/df['ETH Volume'][0], color='Blue')
plt.plot(df['Date'],df['BTC Volume']/df['BTC Volume'][0], color='Orange')
plt.show()

plt.plot(df['Date'],df['DOGE Volume']/df['DOGE Volume'][0], color='Blue')
plt.plot(df['Date'],df['BTC Open']/df['BTC Volume'][0], color='Orange')
plt.show()

# comparing Ethereum with BAT, which is ETH-based
plt.plot(df['Date'],df['BAT Open']/df['BAT Open'][0], color='Blue') # plotting price relative to initial price
plt.plot(df['Date'],df['ETH Open']/df['ETH Open'][0], color='Orange')
plt.show()

plt.plot(df['Date'],df['BAT Volume']/df['BAT Volume'][0], color='Blue') # plotting volume relative to initial volume
plt.plot(df['Date'],df['ETH Volume']/df['ETH Volume'][0], color='Orange')
plt.show()

# comparing Dogecoin with Categorical Elon Musk Twitter Data
plt.plot(df['Date'],df['DOGE Open']/df['DOGE Open'][0], color='Blue', linewidth=2)
for i in range(len(df['Date'])):
    if (df['Elon Tweet?'][i] == "yes"):
        plt.axvline(x= df['Date'][i], color='Orange', zorder=1, linewidth=1)
plt.show()

# comparing coins with Dow Jones Data
plt.plot(df['Date'],df['ETH Open']/df['ETH Open'][0], color='White')
for j in range(len(df['Date'])):
    if pd.isna(df['DJ Change'][j]) == False:
        if df['DJ Change'][j] == "increase":
            plt.axvline(x=df['Date'][j], color='Green', zorder=1, linewidth=10)
        elif df['DJ Change'][j] == "decrease":
            plt.axvline(x=df['Date'][j], color='Red', zorder=1, linewidth=10)
        else:
            plt.axvline(x=df['Date'][j], color='Yellow', zorder=1, linewidth=1) # I made stagnant zones less visible for better readability
plt.show()

plt.plot(df['Date'],df['DOGE Open']/df['DOGE Open'][0], color='White')
for j in range(len(df['Date'])):
    if pd.isna(df['DJ Change'][j]) == False:
        if df['DJ Change'][j] == "increase":
            plt.axvline(x=df['Date'][j], color='Green', zorder=1, linewidth=10)
        elif df['DJ Change'][j] == "decrease":
            plt.axvline(x=df['Date'][j], color='Red', zorder=1, linewidth=10)
        else:
            plt.axvline(x=df['Date'][j], color='Yellow', zorder=1, linewidth=1)
plt.show()

# running regressions for more conclusive details on relationships
x = df['BTC Open']/df['BTC Open'][0]
y = df['ETH Open']/df['ETH Open'][0]

print(y.corr(x))

a = df['BAT Open']/df['BAT Open'][0]

print(a.corr(x))

b = df['DOGE Open']/df['DOGE Open'][0]

print(b.corr(x))

print(a.corr(y))

