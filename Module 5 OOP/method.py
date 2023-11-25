class phone:
    price=1200
    color='blue'
    brand = 'samsung'
    feature = ['camera','speaker','hammer']
    def call(self):
        print('calling one person')
    
    def send_sms(self,phone,sms):
        text = f'sending SMS TO : {phone} and message : {sms}'
        return text
my_phone = phone()
print(my_phone.feature)
my_phone.call()
result = my_phone.send_sms(21121,1321)
print(result)