import phonenumbers
from phonenumbers import geocoder


# | Country             | Example Number | Country Code |
# | ------------------- | -------------- | ------------ |
# | 🇧🇩 Bangladesh     | +8801712345678 | +880         |
# | 🇺🇸 USA            | +14155552671   | +1           |
# | 🇬🇧 United Kingdom | +447911123456  | +44          |
# | 🇮🇳 India          | +919876543210  | +91          |
# | 🇩🇪 Germany        | +4915123456789 | +49          |


def get_country_from_local_number(number, default_region="BD"):
    try:
        parsed = phonenumbers.parse(number, default_region)

        if not phonenumbers.is_valid_number(parsed):
            return {"error": "Invalid phone number."}

        country_name = geocoder.description_for_number(parsed, "en")
        region_code = phonenumbers.region_code_for_number(parsed)

        return {
            "international_format": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
            "country_name": country_name,
            "region_code": region_code
        }
    except phonenumbers.NumberParseException as e:
        return {"error": str(e)}

# Example usage
phone = "+447911123456"
info = get_country_from_local_number(phone)
print(info)
