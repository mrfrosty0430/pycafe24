
import pycafe24
from pycafe24.oauth2 import Cafe24Credentials
from pycafe24.cache import Cache
from pycafe24.functions import Cafe24Client

import webbrowser



cafe24_client = Cafe24Credentials(
	mall_id="mrfrosty0430",
	client_id="gbOWY016IpvpYhRXrjoefD",
	client_secret="efuboDbeKpq3dDdYzrMrGa",
	csrf_token=None,
	redirect_uri="https://www.incento.kr/connect",
	scope="mall.read_order,mall.write_order,mall.read_customer,mall.write_customer,mall.read_promotion,mall.write_promotion,mall.write_application,mall.read_application",
	cache_handler=Cache(cache_path="pycafe24/cache/mrfrosty0430")
	)

# print(cafe24_client.has_valid_access_token())
# print(cafe24_client.has_valid_refresh_token())

# cafe24_client.update_refresh_token()

# print(cafe24_client.has_valid_access_token())
# print(cafe24_client.has_valid_refresh_token())

# if True:
if not cafe24_client.cache_handler:
	response_url = cafe24_client.get_authentication_code()
	chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
	webbrowser.get(chrome_path).open(response_url)
	code = input("client code is ")
	# #
	cafe24_client.get_access_code(code)
#

pycafe24_client = Cafe24Client(credentials_manager=cafe24_client)
# response = pycafe24_client.update_scripttag("1657064027462669")
# response = pycafe24_client.update_scripttag("1658103536675629")
# response = pycafe24_client.create_scripttag(["MEMBER_JOINRESULT"],
# 	src="https://referral-bucket-test.s3.ap-northeast-2.amazonaws.com/register_success.js",
# 	exclude_path=[]
# )
# print(response.json())
#
# response = pycafe24_client.create_scripttag(["all"],
# 	src="https://referral-bucket-test.s3.ap-northeast-2.amazonaws.com/main.js",
# 	exclude_path=["/member/join_result.html"]
# )
# print(response.json())
# # response = pycafe24_client.list_issue_coupon(6072880254000000104)
# # response = pycafe24_client.issue_coupon(6073129886000000184,"M",
# # 	member_id="sungjunh")
# # response = pycafe24_client.count_customer_coupon("sungjunh")
# # response = pycafe24_client.delete_customer_coupon("sungjunh",6072880254000000104)
# # print(response.json())
# response = pycafe24_client.list_scripttag()
# print(response.json())

response = pycafe24_client.list_customer_coupon("hongs")
print(response.json())

#
# response = pycafe24_client.update_scripttag(1659335204303465,
# 	src="https://referral-bucket-test.s3.ap-northeast-2.amazonaws.com/main.js",
# 	display_location=["all"],
# 	exclude_path=["/member/join_result.html"]
# )
# print(response.json(),"\n\n")
# response = pycafe24_client.update_scripttag(1659335204179143,
# 	src="https://referral-bucket-test.s3.ap-northeast-2.amazonaws.com/register_success.js",
# 	display_location=["MEMBER_JOINRESULT"],
# 	exclude_path=[]
# )
# print(response.json(),"\n\n")

# response = pycafe24_client.create_coupon("테스트쿠폰","A","M","M",None,None,None,None,"O","U",None,"U",None,"E",1,None,None,None,None,None)
# print(response.json())
# code = input("client code is")
