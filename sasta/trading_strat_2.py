from trades import get_trades, get_csticks, get_closePriceNTime,get_bands
import matplotlib.pyplot as plt
import numpy
def trade_long(t_entry,t_max,bands,budget,stoploss_percent):
    buy_price=float((get_trades('BNBUSDT','1m',1,None,t_entry))[0][4])
    buy_quant=budget/buy_price
    stoploss_price=stoploss_percent/100*buy_price
    interval=60000
    t=t_entry+interval
    i=0
    while True:
        if int(t_max)-int(t)<=720*interval:
            cdata=get_trades('BNBUSDT','1m',(t_max-t)//interval)
            
        else:
            cdata=get_trades('BNBUSDT','1m',720,t-interval+1000)
        for elem in cdata:
            cp=float(elem[4])
            if cp<stoploss_price:
                t_exit=t
                sp=cp
                profit=(sp-buy_price)*buy_quant
                print('Exit')
                print(sp/buy_price)
                return profit,t_exit
            else:
                t+=interval
                   
            print((t_max-t)//interval) 
            if stoploss_percent*cp/100>stoploss_price:
                stoploss_price=stoploss_percent*cp/100    
            if int(t)==int(t_max):
                return "Not Sold Yet",t
                
    # for i in range(t+1,len(close_list)):
    #     curr_price=float(close_list[i])
    #     markers.append(0)
    #     if curr_price<stoploss_price :
    #         #print(curr_price/buy_price)
    #         sell_price =curr_price
    #         profit=(sell_price-buy_price)*buy_quant
    #         return profit,i+1
    #     if 0.95*curr_price>stoploss_price:
    #         stoploss_price=0.95*curr_price
    # return "Not sold yet",len(close_list)  




def backtest_(budget=1000,stoploss_percent=95):
    
    trade_data=get_trades('BNBUSDT','4h','1000',)
    t_list,t_time=get_closePriceNTime(trade_data)
    bands = get_bands(t_list) 
    count1=0
    trade_success1=0
    i=19
    profit1=0.0
    profit1_list=[]
    t=int(t_time[19])
    t_max=int(t_time[-1]) 
    interval=60000
    flag=1
       
    while True:
        
        curr_data=get_trades('BNBUSDT','1m',720,t-interval+1000)
        prev=t-t_max
        
        for elem in curr_data:
            cp=float(elem[4])
            if cp>=numpy.interp(t,t_time[19:],bands[0][19:]):
                print('entered')
                t_entry=t
            
                profit1,t_exit=trade_long(t_entry,t_max,bands,budget,stoploss_percent)
                t=t_exit
                count1+=1
                if type(profit1) != str:
                    budget+=profit1
                    profit1_list.append(profit1)
                    if profit1>0:
                        trade_success1+=1
            else:
                t+=interval
                print(i)
                print(t,t_max)
                #increment by 1 minute
                i+=1   
            if t>t_max:
                print(t,t_max)
                break       
        
        print(t,t_max)
        if t>t_max:
            
            break
        
        final=t-t_max
        if prev==final:
            flag-=1
        if flag==0:
            break        
    return count1,trade_success1,profit1_list


