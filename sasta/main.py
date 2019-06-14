from trades import get_trades,plot_graph,get_bands,get_csticks,get_closePriceNTime

from trading_strat_2 import backtest_
sym='BNBUSDT'
interval='4h'
limit='100'
trade_data=get_trades(sym,interval,limit)
#print(trade_data)
csticks = get_csticks(trade_data)

t_list,t_timeclose=get_closePriceNTime(trade_data)
bands = get_bands(t_list) 

#markers=TS.backtest_()
#plot_graph(markers,bands,csticks,t_time) 
#print(t_timeclose,t_timeopen)  

c,t,p=backtest_(1000,95,limit)
print(c,t,p,sum(p))        