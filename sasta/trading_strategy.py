from trades import get_trades, get_csticks, get_closePriceNTime,get_bands
import matplotlib.pyplot as plt
def trade_long(t,close_list,bands,budget,markers):
    buy_price=float(close_list[t])
    buy_quant=budget/buy_price
    stoploss_price=0.95*buy_price
    
    for i in range(t+1,len(close_list)):
        curr_price=float(close_list[i])
        markers.append(0)
        if curr_price<stoploss_price :
            #print(curr_price/buy_price)
            sell_price =curr_price
            profit=(sell_price-buy_price)*buy_quant
            return profit,i+1
        if 0.95*curr_price>stoploss_price:
            stoploss_price=0.95*curr_price
    return "Not sold yet",len(close_list)    
    
def trade_short(t,close_list,bands,budget,markers):
    sell_price=float(close_list[t])
    sell_quant=budget/sell_price
    stoploss_price=0.95*sell_price
    
    for i in range(t+1,len(close_list)):
        curr_price=float(close_list[i])
        markers.append(0)
        if curr_price>stoploss_price:
            print(curr_price/sell_price)
            buy_price =curr_price
            profit=(sell_price-buy_price)*sell_quant

            return profit,i+1
        if 1.0*curr_price<stoploss_price:
            stoploss_price=0.95*curr_price
    return "Not sold yet",len(close_list)    

def backtest_(budget,stoploss_percent):
    for inox in range(0,1):
        trade_data=get_trades('BNBUSDT','4h','1000',str(1543604400000+(inox*2592000000)),str(1543604400000+((inox+1)*2592000000)))
        csticks = get_csticks(trade_data)
        t_list,t_time=get_closePriceNTime(trade_data)
        bands = get_bands(t_list) 
        #print(bands[2])
        count1=0
        # count2=0
        trade_success1=0
        # trade_success2=0
        i=19
        profit1=0.0
        # flag=0
        profit1_list=[]
        # profit2_list=[]
        
        # markers=[]
        print(len(csticks[3]))
        while i<len(csticks[3]):
            cp=float(csticks[3][i])
            if cp>=float(bands[0][i]):
                
                # markers.append(cp)
                profit1,j=trade_long(i,bands,budget,stoploss_percent)
                
                i=j
                count1+=1
                if type(profit1) != str:
                    budget+=profit1
                    profit1_list.append(profit1)
                    if profit1>0:
                        trade_success1+=1
        #    elif cp<float(bands[2][i]):
        #         markers.append(cp)
        #         profit2,q=trade_short(i,csticks[3],bands,budget,markers)
        #         i=q
        #         count2+=1
        #         if type(profit2) != str:
        #             budget+=profit2
        #             profit2_list.append(profit2)
        #             if profit2>0:
        #                 trade_success2+=1
            
            else:
                # markers.append(0)
                i+=1        
        print(count1,trade_success1,'\n',profit1_list,'\n', sum(profit1_list))
        #print(count2,trade_success2,'\n',profit2_list,'\n', sum(profit2_list))
    return None
backtest_(1000,95)    