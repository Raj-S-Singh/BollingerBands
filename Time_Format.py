import time
#timestamp=[1559807999999]

def FormatTime(timestamp):
    
    for i in range(0,len(timestamp)):

        time_element=timestamp[i]

        

        time_element=time.ctime(int(time_element*0.001))

        
        time_element=time_element.split(" ")


        if time_element[2]=='':
            del time_element[2]
            time_element[2]="0"+time_element[2]

        time_element[3]=time_element[3].split(":")

        time_element[3]=time_element[3][0]+":"+str(int(time_element[3][1])+1)

        time_element=time_element[3]+"\n"+time_element[1]+" "+time_element[2]
        
        

        timestamp[i]=time_element


    
    return timestamp

#FormatTime(timestamp)