from audioop import add
import re

def isE164(number):
    if not number:
        return False
    number=("+","")[number[0]=="+"]+number
    return re.match(r"^\+?[1-9]\d{1,14}$",number) is not None

def isWechat(number):
    if not number or len(number)<1 or len(number)>248:
        return False
    return re.match(r"^[a-zA-Z0-9+-_@.]*$",number) is not None

def validatePhoneNumberFormat(address):
    if isE164(address):
        return "SMS"
    
    val=address.split(":")
    if len(val)!=2:
        return "INVALID_ADDRESS"
    
    provider=str.upper(val[0])
    if provider in ["WHATSAPP","MESSENGER"] and isE164(val[1]):
        return provider
    elif provider=="WECHAT" and isWechat(val[1]):
        return provider
    
    return "INVALID_ADDRESS"

print(validatePhoneNumberFormat("+15555555555"))
print(validatePhoneNumberFormat("15555555555"))
print(validatePhoneNumberFormat("+15555555555555555"))
print(validatePhoneNumberFormat("whatsapp:15555555555"))
print(validatePhoneNumberFormat("wechat:identifier:ghke83772"))
print(validatePhoneNumberFormat("wechat:ghke83772"))
print(validatePhoneNumberFormat("whatsapp:+15555555555"))
print(validatePhoneNumberFormat("messenger:15555555555"))
print(validatePhoneNumberFormat("messenger:+15555555555"))
print(validatePhoneNumberFormat("messenger:+15555555555555555"))
print(validatePhoneNumberFormat("whatsapp:this_is_not_an_E164_number"))
print(validatePhoneNumberFormat("messenger:this_is_not_an_E164_number"))
print(validatePhoneNumberFormat("wechat:this_is_alphanumeric_with_special_character"))