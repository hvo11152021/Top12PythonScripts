import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_phone_data(number):
    phoneNumber = phonenumbers,parse(number)
    return {
        "basisc-data": phoneNumber,
        "time-zone": timezone.time_zones_for_number(phoneNumber),
        "carrier": carrier.name_for_number(phoneNumber, "en"),
        "is_valid": phonenumbers.is_valid_number(phoneNumber),
        "is_possible": phonenumbers.is_possible_number(phoneNumber),
    }

print(get_phone_data("+91XXXXXXXXXX"))