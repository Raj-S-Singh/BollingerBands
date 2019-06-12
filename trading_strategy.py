from trades import get_trades, get_csticks, get_closePriceNTime,get_bands
import matplotlib.pyplot as plt
import calculate_CurrBands as CCB

def trade_long(curr_closePrice,cur_Upperband,budget):
    buy_price=curr_closePrice
    buy_quant=budget/buy_price
    stoploss_price=0.95*buy_price
    
    for i in range(t+1,len(close_list)):
        curr_price=float(close_list[i])
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
    stoploss_price=1.05*sell_price
    
    for i in range(t+1,len(close_list)):
        curr_price=float(close_list[i])
        markers.append(0)
        if curr_price>stoploss_price:
            print(curr_price/sell_price)
            buy_price =curr_price
            profit=(sell_price-buy_price)*sell_quant

            return profit,i+1
        if 1.05*curr_price<stoploss_price:
            stoploss_price=1.05*curr_price
    return "Not sold yet",len(close_list)    

def backtest_():
    for inox in range(0,1):
        trade_data=get_trades('BNBUSDT','4h','100')
        csticks = get_csticks(trade_data)
        t_list,t_time=get_closePriceNTime(trade_data)
        bands,t_time = get_bands(t_list,t_time)
        #print(bands)
        count1=0
        count2=0
        trade_success1=0
        trade_success2=0
        i=19
        profit1=0.0
        flag=0
        profit1_list=[]
        profit2_list=[]
        budget=1000
        markers=[]
        #print(len(csticks[3]))
        flag=1
        for f in trade_data:
            if flag<20:
                flag+=1
                print("flag=>",flag)
            else:
                flag+=1
                print("flag=>",flag)
                trade_open=f[0]
                trade_close=f[6]
                print(trade_close,trade_open)
                for f in range(trade_open,trade_close+1,60000):
                    print("f=>",f)
                    Comp_trade_data=get_trades('BNBUSDT','1m','1',str(f),str(f+60000))
                    #print(Comp_trade_data)
                    curr_closePrice=float(Comp_trade_data[0][4])
                    crr_timeStamp=Comp_trade_data[0][6]
                    cur_UpperBand=CCB.Calculate_UpperBandvalue(trade_data,crr_timeStamp,bands[0],t_time)
                    #print(cp)
                    if curr_closePrice>=cur_UpperBand:
                        #profit1=trade_long(curr_closePrice,cur_UpperBand,budget)
                        count1+=1
                        print("Enteredcount=>",count1)
                        buy_price=curr_closePrice
                        buy_quant=budget/buy_price
                        stoploss_price=0.95*buy_price
                        for f in range(crr_timeStamp,trade_close+1,60000):
                            Comp_trade_data=get_trades('BNBUSDT','1m','1',str(f),str(f+60000))
                    #print(Comp_trade_data)
                            curr_closePrice=float(Comp_trade_data[0][4])
                            crr_timeStamp=float(Comp_trade_data[0][6])
                            cur_UpperBand=CCB.Calculate_UpperBandvalue(trade_data,crr_timeStamp,bands[0],t_time)
                    #print(cp)
                            curr_price=curr_closePrice
                            if curr_price<stoploss_price :
            #print(curr_price/buy_price)
                                sell_price =curr_price
                                profit=(sell_price-buy_price)*buy_quant
                                print(profit)
                                profit1_list.append(profit)
                                if profit>0:
                                    trade_success1+=1
                                    print("Exit=>",trade_success1)
                                break
                            if 0.95*curr_price>stoploss_price:
                                stoploss_price=0.95*curr_price
                                
    
                        #profit1=trade_long(curr_closePrice,cur_UpperBand,budget)
                        # count1+=1
                        # buy_price=curr_closePrice
                        # buy_quant=budget/buy_price
                        # stoploss_price=0.95*buy_price
                        # if type(profit1) != str:
                        #     budget+=profit1
                        #     profit1_list.append(profit1)
                        #     if profit1>0:
                        #         trade_success1+=1
        
        # while i<len(csticks[3]):
        #     cp=float(csticks[3][i])
        #     if cp>=float(bands[0][i]):
                
                
        #         markers.append(cp)
        #         profit1,j=trade_long(i,csticks[3],bands,budget,markers)
                
        #         i=j
        #         count1+=1
        #         if type(profit1) != str:
        #             budget+=profit1
        #             profit1_list.append(profit1)
        #             if profit1>0:
        #                 trade_success1+=1
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
            
    #         else:
    #             markers.append(0)
    #             i+=1        
    #     print(count1,trade_success1,'\n',profit1_list,'\n', sum(profit1_list))
    #     #print(count2,trade_success2,'\n',profit2_list,'\n', sum(profit2_list))
    # return markers

backtest_()