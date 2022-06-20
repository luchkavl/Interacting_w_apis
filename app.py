from libs.openexchange import OpenExchangeClient

APP_ID = '1d08179cda32468f816c63ec3e80bbc8'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print(f'USD {usd_amount} is GBP {gbp_amount:.2f}')
