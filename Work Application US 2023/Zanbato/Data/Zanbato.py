from tempfile import tempdir
import pandas as pd


def question1(file_name):
    df=pd.read_csv(file_name)
    # print("before sorting")
    # print(df.head(10))
    df.sort_values(df.columns[10], 
                    axis=0,
                    ascending=[False],
                    inplace=True)
    # print("after sorting")
    # print(df.head(10))

    month_dict={1:"January", 2:"February", 3:"March", 4:"Apirl", \
        5:"May", 6:"June", 7:"July", 8:"August", 9:"September",\
             10:"October", 11:"November", 12:"December"}
    res_temperature=[str(df.iloc[0,10])]

    res=[res_temperature[0]+', '+df.iloc[0,5]+', '\
        +month_dict[df.iloc[0,2]]+' '+str(df.iloc[0,3])]

    for i in range(1,len(df)):
        if df.iloc[i,10]!=int(res_temperature[i-1]):
            break
        else:
            res_temperature.append(str(df.iloc[i,10]))
            res.append(res_temperature[i]+', '+df.iloc[i,5]+', '\
                +month_dict[df.iloc[i,2]]+' '+str(df.iloc[i,3]))
    return res


def question2(file_name):
    df=pd.read_csv(file_name)
    res_dict={}
    for i in range(len(df)):
        if df.iloc[i,8] not in res_dict:
            res_dict[df.iloc[i,8]]=float("-inf")
    for i in range(len(df)):
        res_dict[df.iloc[i,8]]=max(res_dict[df.iloc[i,8]],df.iloc[i,-1])
    # wind_speed=list(res_dict.values())
    # wind_speed.sort()
    # print(wind_speed)
    return res_dict

    # df=pd.read_csv(file_name)
    # df.sort_values(df.columns[-1], 
    #                 axis=0,
    #                 ascending=[False],
    #                 inplace=True)
    # for i in range(100):
    #     print(df.iloc[i,8])
    # print(df.head(100))


# print(question1("weather.csv"))

print(question2("weather.csv"))


    