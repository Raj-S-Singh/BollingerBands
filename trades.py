import requests
from numpy import asarray
import numpy as np  
from talib._ta_lib import BBANDS
import plotly as plt
from Bollinger_Bands.Time_Format import FormatTime
from plotly.graph_objs import Scatter,Layout,Candlestick



def get_trades(sym,span,lim):
    '''Returns the list containing the trade data for the given symbol, interval and limit as obtained from the api'''
    dsrc="https://api.binance.com/api/v1/klines?symbol="+sym+"&interval="+span+"&limit="+lim
    resp = requests.get(dsrc)
    #resp=request.get("https://api.binance.com/api/v1/klines?symbol=BNBUSDT&interval=4h&limit=1000")
    #resp=requests.get("https://test.deribit.com/api/v2/public/get_tradingview_chart_data?end_timestamp=1554376800000&instrument_name=BTC-PERP&resolution=30&start_timestamp=1554373800000")
    #resp=requests.get("https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10")
    #resp = requests.get("https://test.deribit.com/api/v2/public/get_last_trades_by_instrument?count=1&instrument_name=BTC-PERPETUAL")

    trade_data=resp.json()
    return trade_data

def get_current_price(sym):
    '''Returns the current price for the given symbol'''
    dsrc="https://api.binance.com/api/v3/ticker/price?symbol="+sym
    resp=requests.get(dsrc)
    current_price=resp.json()['price']
    return current_price
    
    
def get_closePriceNTime(trade_data):
    '''Returns a tuple containing the closing price and timestamp for an interval'''
    trade_close=[]
    trade_time=[]
    for trade in trade_data:
        trade_close.append(float(trade[4]))
        trade_time.append(FormatTime([trade[6]])[0])
    return (trade_close,trade_time)

def get_csticks(trade_data):
    '''Returns a list containing the open, high, low, and close prices of the commodity '''
    csticks=[[],[],[],[]]
    
    for i in range(len(trade_data)):
        for j in range(4):
            csticks[j].append(trade_data[i][j+1])
            
    return csticks

def get_bollinger_bands(trade_list,duration=20,multiplier=2):   
    '''Gives the upper, middle and lower bands for the given list, no. of days(duration) and multiplier '''
    trade_array=asarray(trade_list)
    return BBANDS(trade_array,duration,multiplier,multiplier,0)

def get_bands(t_list):
    '''Returns the list of upper, middle and lower bands for std dev multiplier 2 and 1''' 
    b = []
    for i in range(len(t_list)*3):
        b.append(0)
    bands = []
    for i in range(2):
        b[3 * i + 0], b[3 * i + 1], b[3 * i + 2] = get_bollinger_bands(t_list, 20, i + 1)
    
    for i in range(6):
        bands.append(b[i])
    
    return bands
        
def plot_graph(bands,csticks,time_list):
    '''Plots the bollinger bands and the candlesticks on the same plot'''
    trace=bands
    
    data=[]
    
    for i in range(len(bands)):
        trace[i]=Scatter(x=time_list,y=np.ndarray.tolist(bands[i]))
        data.append(trace[i])
    data[4]=Candlestick(x=time_list,open=csticks[0],high=csticks[1],low=csticks[2],close=csticks[3])    
    
    plt.offline.plot({"data":data,"layout":Layout(title="SMA w Bollinger Bands")})
       
        
#get_trades,plot_graph,get_bands,get_csticks,get_close,get_trades    

