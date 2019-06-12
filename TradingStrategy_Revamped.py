import numpy as np
import trades 
import Check_LongTrade as CLT
import time

class TradingStrategy:
        def __init__(self,Budget,List_ClosePrice,List_OpenTime,List_CloseTime,List_Bands,interval=1):
                self.List_ClosePrice=List_ClosePrice
                self.List_OpenTime=List_OpenTime
                self.List_CloseTime=List_CloseTime
                self.List_Bands=List_Bands
                self.interval=1
                self.trade_entered=0
                self.trade_successs=0
                self.trade_data=[]
                self.Array_CloseTime=np.array([])
                self.Array_upperBand=np.array([])
                self.Array_ClosePrice=np.array([])
                self.profit=0
                self.balance=Budget
                self.counter=0
                self.List_Dict_tradeDetails=[]
        
        def  CheckEveryMinute(self):
                for i in range(0,len(self.List_CloseTime),3):
                        print(i)
                        if i+3>len(self.List_OpenTime)-1:
                                break
                        self.counter=0
                        self.trade_data=trades.get_trades('BNBUSDT','1m','720',str(self.List_OpenTime[i]),str(self.List_CloseTime[i+3]))
                        self.trade_data=np.array(self.trade_data)
                        self.Array_CloseTime=self.trade_data[:,6]
                        self.Array_CloseTime=[int(i) for i in self.Array_CloseTime]
                        
                        self.Array_ClosePrice=self.trade_data[:,4]
                        # print("\n Array_CloseTime=>",np.array(self.Array_CloseTime))
                        # print("\n List Close Time",self.List_CloseTime)
                        # print("\nLsit_Bands=>",self.List_Bands[0])

                        
                        self.Array_upperBand=np.interp(np.array(self.Array_CloseTime),self.List_CloseTime,self.List_Bands[0])
                        for self.counter in range(0,len(self.trade_data)):
                                #print("HO!",self.trade_data[self.counter][4],"\nHO2",self.Array_upperBand[self.counter])
                                if float(self.trade_data[self.counter][4])>=float(self.Array_upperBand[self.counter]):
                                        TradeEnterTime=self.Array_CloseTime[self.counter]
                                        buy_Price=float(self.trade_data[self.counter][4])
                                        buy_Quant=float(self.balance)/buy_Price
                                        price_stoploss=0.95*buy_Price
                                        print("Counter1=>",self.counter)
                                        (profit,close_Price)=self.Execute_LongTrade(price_stoploss,buy_Quant,buy_Price)
                                        if close_Price!=None:
                                                print("Counter2=>",self.counter)
                                                self.balance+=profit
                                                self.profit+=profit
                                                TradeExitTime=self.Array_CloseTime[self.counter]
                                                Dict_trade={'Trade Enter Time':TradeEnterTime,
                                                'Buy Price':buy_Price,'Quantity Traded': buy_Quant,
                                                'Profit/Loss':profit,'Trade Sell Time':TradeExitTime,
                                                'Sell Price' :close_Price, 'Trade Time':(str((TradeExitTime-TradeEnterTime)*0.001/3600)+'Hrs')}
                                                self.List_Dict_tradeDetails.append(Dict_trade)


        def Execute_LongTrade(self,price_stoploss,buy_quant,buy_Price):
                for self.counter in range(self.counter+1,len(self.trade_data)):
                        #print("YO BITCH")
                        curr_price=float(self.Array_ClosePrice[self.counter])
                        if curr_price<price_stoploss or curr_price<=buy_Price:
                                sell_price=curr_price
                                profit=(sell_price-buy_Price)*buy_quant
                                print(profit,sell_price)
                                return (profit,sell_price)

                        if 0.95*curr_price>price_stoploss:
                                price_stoploss=0.95*curr_price
                return "Not Sold Yet",None    
                
        def GetBacktestDetails(self):
                print(self.List_Dict_tradeDetails)
                print("Profit=>",self.profit)      
                print("Balance=>",self.balance)       

"""def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    def CalculateProfit_LongTrade(i,budget,Array_upperBand,trade_data):
        trade_data=trade_data[:,4]
        for i in range(i,len(trade_data)):
            if trade_data[i]>=Array_upperBand[i]:
                buy_price=float(trade_data[i])
                buy_quant=budget/buy_price
                stoploss_price=0.95*buy_price
                
                pass
            else:
                pass"""
