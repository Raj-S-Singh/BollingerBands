from trades import get_trades,plot_graph,get_bands,get_csticks,get_closePriceNTime
import trading_strategy  as TS
trade_data=get_trades('BNBUSDT','4h','1000','sasda','asas')
csticks = get_csticks(trade_data)

t_list,t_time=get_closePriceNTime(trade_data)
bands = get_bands(t_list) 
markers=TS.backtest_()
plot_graph(markers,bands,csticks,t_time)   

