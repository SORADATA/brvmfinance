
BASE_URL = "https://www.sikafinance.com/api/charting/GetTicksEOD"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.sikafinance.com/',
    'Accept': 'application/json',
}


def get_faux_guid(length=30):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))