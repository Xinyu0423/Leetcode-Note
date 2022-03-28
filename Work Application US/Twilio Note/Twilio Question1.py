
def validateImageSuze(imageurls,maxSize):
    if maxSize=="None":
        size=1
        unit="MB"
    else:
        size=int(maxSize[:-2])
        unit=str.upper(maxSize[-2:])
    print("unit=",unit)
    # print("size=",size)
    digit_level=(["KB","MB","GB"].index(unit)+1)
    print("digit_level=",digit_level)
    if unit=="KB":
        size*=1000
    elif unit=="MB":
        size*=1000000
    elif unit=="GB":
        size*=1000000000
    for i,(_,img_size) in enumerate(imageurls):
        if len(img_size)<digit_level:
            imageurls[i][1]="TRUE"
        else:
            # print(img_size[:digit_level])
            # print(img_size[-digit_level:])
            # unit_size=float(img_size[:digit_level]+"."+img_size[-digit_level:])
            imageurls[i][1]=("TRUE","FALSE")[int(img_size)>size]
    # print(unit_size)
    return imageurls

image_Url1=validateImageSuze([['https://svs.gsfc.nasa.gov/vis/a030000/a030800/a030877/fr ames/5760x3240_16x9_01p/BlackMarble_2016_928m_conus_labeled . png','32000000']],'20MB')
print(image_Url1)
image_Url2=validateImageSuze([['https://svs.gsfc.nasa.gov/vis/a03000Θ/a030800/a030877/fr ames/5760x3240_16x9_01p/BlackMarble_2016_928m_conus_labeled · png','32000000']],'40MB')
print(image_Url2)