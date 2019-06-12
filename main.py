from trades import get_trades,plot_graph,get_bands,get_csticks,get_closePriceNTime

from TradingStrategy_Revamped import TradingStrategy

trade_data=get_trades('BNBUSDT','4h','100')
#print(trade_data)
csticks = get_csticks(trade_data)

t_list,t_timeclose,t_timeopen=get_closePriceNTime(trade_data)
bands,t_timeclose = get_bands(t_list,t_timeclose) 

#markers=TS.backtest_()
#plot_graph(markers,bands,csticks,t_time) 
#print(t_timeclose,t_timeopen)  

BackTest=TradingStrategy(1000,t_list[19:],t_timeopen,t_timeclose,bands)
BackTest.CheckEveryMinute()
BackTest.GetBacktestDetails()