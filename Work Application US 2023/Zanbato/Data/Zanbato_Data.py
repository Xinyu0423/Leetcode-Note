import pandas as pd

def generateDate(date):
    date = date.split('-')
    month = int(date[1])
    day = int(date[2])
    MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    return '{} {}'.format(MONTH[month-1], day)
    
def findHottest(df):
    Max = -1
    for i in df.index:
        if df.loc[i, 'Data.Temperature.Max Temp'] > Max:
            Max = df.loc[i, 'Data.Temperature.Max Temp']
    for i in df.index:
        if df.loc[i, 'Data.Temperature.Max Temp'] == Max:
            print('{}, {}, {}'.format(Max, df.loc[i, 'Station.Location'].split(',')[0],\
                 generateDate(df.loc[i, 'Date.Full'])))

def highestSpeed(df):
    dic = {}
    for i in df.index:
        state = df.loc[i, 'Station.State']
        speed = df.loc[i, 'Data.Wind.Speed']
        if state not in dic:
            dic[state] = speed
        else:
            dic[state] = max(dic[state], speed)
    print('***************************************')
    for i in dic:
        print('{}: {}'.format(i, dic[i]))

# I did a little bit research about the most comfortable tempature and windspeed
# Found that people feel most comfortable
# when the temperature is around 70 degrees Fahrenheit
# and the wind speed is between 1-5
# So I set 70 degrees Fahrenheit as the baseline for temperature
# and 2.5 as the baseline for wind speed
# (the closer the temperature and wind speed were to 70 and 2.5,
# the higher the score)

# Source for tempature:
# https://www.scientificamerican.com/article/why-people-feel-hot/#:~:text=It%20does%20so%20by%20circulating,temperature%20around%2098%20degrees%20F.
# Source for windspeed:
# https://www.researchgate.net/figure/Wind-speed-and-human-body-feeling-8_tbl1_283944198#:~:text=Table%201%20shows%20the%20different,environment%20for%20human.%20...

def findTopTenNicestPlace(df):
    print('************************************************')
    dic = {}
    for i in df.index:
        city = df.loc[i, 'Station.City']
        if city not in dic:
            dic[city] = (100-abs(df.loc[i, 'Data.Wind.Speed']-2.5)) * 0.5\
                 + (100-abs(70-df.loc[i, 'Data.Temperature.Avg Temp']))*0.5
        else:
            score = (100-abs(df.loc[i, 'Data.Wind.Speed']-2.5)) * 0.5\
                 + (100-abs(70-df.loc[i, 'Data.Temperature.Avg Temp']))*0.5
            dic[city] = max(dic[city], score)
    lst = [(i, dic[i]) for i in dic]
    lst = sorted(lst, key=lambda x:x[1], reverse=True)
    print('The top 10 nicest places to live is: ')
    for i in range(len(lst)):
        print('{}. {} - {:.3f}'.format(i+1, lst[i][0], lst[i][1]))
        if i == 9:
            break

def main(fileName):
    print('*********************************************')
    df = pd.read_csv(fileName)
    findHottest(df)
    highestSpeed(df)
    findTopTenNicestPlace(df)
if __name__ == '__main__':
    main('weather.csv')