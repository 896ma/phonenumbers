import phonenumbers
from test import  number       
 

from phonenumbers  import geoco
ch_numbr =phonenumbers.parse(number ,"CH")
print(geocoder.description_for_number(ch_numbr,"en"))

from phonenumbers import carrier
service_numbr =phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_numbr ,"en"))
