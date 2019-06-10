from Bollinger_Bands.trades import get_trades, get_csticks, get_closePriceNTime,\
    get_bands
from test.test_binop import isnum
def trade_long(t,close_list,bands,budget):
    buy_price=float(close_list[t])
    buy_quant=budget/buy_price
    stoploss_price=0.95*buy_price
    
    for i in range(t+1,len(close_list)):
        curr_price=float(close_list[i])
        if curr_price<=float(bands[1][i]) or curr_price<=stoploss_price:
            print(curr_price/buy_price)
            sell_price =curr_price
            profit=(sell_price-buy_price)*buy_quant
            return profit,i+1
    return "Not sold yet",len(close_list)    
        
trade_data=get_trades('BNBUSDT','4h','1000')
csticks = get_csticks(trade_data)
t_list,t_time=get_closePriceNTime(trade_data)
bands = get_bands(t_list) 
count=0
trade_success=0
i=19
profit=0.0
profit_list=[]
budget=1000
while i<len(csticks[3]):
    cp=float(csticks[3][i])
    if cp>=float(bands[0][i]):
        
        profit,j=trade_long(i,csticks[3],bands,budget)
        
        i=j
        count+=1
        if isnum(profit):
            budget+=profit
            profit_list.append(profit)
            if profit>0:
                trade_success+=1
    else:
        i+=1        
print(count,trade_success,'\n',profit_list,'\n', sum(profit_list))        