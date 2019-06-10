from Bollinger_Bands.trades import get_trades,plot_graph,get_bands,get_csticks,get_closePriceNTime

trade_data=get_trades('BNBUSDT','4h','1000')
csticks = get_csticks(trade_data)

t_list,t_time=get_closePriceNTime(trade_data)
bands = get_bands(t_list) 
plot_graph(bands,csticks,t_time)   
