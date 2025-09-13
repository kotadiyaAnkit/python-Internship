import phonenumbers
from phonenumbers import geocoder

phonenumbers1 = phonenumbers.parse("+91 93134 21232")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phonenumbers1, "en"));