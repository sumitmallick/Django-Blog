from facebookads.api import FacebookAdsApi
from facebookads.objects import AdAccount, Ad, Insights, AdUser
import datetime


my_app_id = '859559060882432'
my_app_secret = '814003e084c93a5ac471f6cf49419742'
my_access_token = 'EAAMNw7B8xAABALEzf2PEMGcpcVxpZBrcDHYfWUhL1ME9Yx9NkJxq63fowCZAZAOdvZC9oSD4jUFSd8mWUCtPP9osiokkZCcsj9yR0NNtnlNIX5cZCZC6CsR1KNT42WdQKIbFJh94Ag6XWEAn7iHNSIjgGIpzLh1pusZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = AdUser(fbid='me')
my_accounts = list(me.get_ad_accounts())
my_account = my_accounts[0]

fields = [
    Insights.Field.campaign_name,
    Insights.Field.spend
]

params = {
    'time_range': {'since': str(datetime.date(2015, 1, 1)), 'until': str(datetime.date.today())},
    'level': 'campaign',
    'limit': 1000
}
