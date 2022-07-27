import csv

def find_hottest(messageList):
    Max=-1
    for i in messageList:
        if int(i[10])>Max:
            Max=int(i[10])
    print('{:30}{:30}'.format('Station.Location','Data.Full'))
    for i in messageList:
        if int(i[10])==Max:
            print('{:30}{:30}'.format(i[7],i[1]))

def highestSpeed(messageList):
    dic={}
    for i in messageList:
        if i[8] not in dic:
            dic[i[8]]=float(i[-1])
        else:
            dic[i[8]]=max(dic[i[8]],float(i[-1]))
    print("***************************")
    print('{:30}{:30}'.format("Station.State","Data.Wind.Speed"))
    for i in dic:
        print("{:30}{:30}".format(i,dic[i]))

def topTenPlace(messageList):
    print("***********************************")
    dic={}
    for i in messageList:
        if i[5] not in dic:
            dic[i[5]]=(100-abs(float(i[-1])-2.5))*0.5+(100-abs(70-int(i[9])))*0.5
        else:
            score=(100-abs(float(i[-1])-2.5))*0.5+(100-abs(70-int(i[9])))*0.5
            dic[i[5]]=max(dic[i[5]],score)
    lst=[(i,dic[i]) for i in dic]
    lst=sorted(lst,key=lambda x:x[1], reverse=True)
    print("The top 10 nicest places to live are")
    for i in range(len(lst)):
        print(lst[i][0],"{:.2f}".format(lst[i][1]))
        if i==9:
            break
    
def main(fileName):
    print('*******************************')
    messageList=[]
    with open(fileName,'r') as file:
        first=True
        for i in file:
            if first is True:
                first=False
                continue
            messageList.append(i.split('\",'))
            for j in range(len(messageList[-1])):
                messageList[-1][j]=messageList[-1][j].replace('\"','')
            messageList[-1][7]=messageList[-1][7].split(',')[0]
    find_hottest(messageList)
    highestSpeed(messageList)
    topTenPlace(messageList)
if __name__=='__main__':
    main("weather.csv")


