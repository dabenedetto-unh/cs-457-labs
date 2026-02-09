
# 1. Phone Cleaner
def phone_cleaner(phone_list):
    cleaned = []
    for phone in phone_list:
        digits = "".join([char for char in phone if char.isdigit()])
        cleaned.append(digits)
    return cleaned

# 2. Email Domain Extractor
def domain_extractor(emails):
    counts = {}
    for email in emails:
        domain = email.split('@')[-1]
        counts[domain] = counts.get(domain, 0) + 1
    return counts

# 3. Currency Converter
def parse_currency(price_strings):
    floats = []
    for price in price_strings:
        clean_price = price.replace('$', '').replace(',', '')
        floats.append(float(clean_price))
    return floats
