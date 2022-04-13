import os
from pyjiracloudapi import jiracloudApi

iurl = "https://my_domain.atlassian.net/rest/api/3"
ijson = ""
imethod="GET"
iapi = "/dashboard"
iuseremail= os.environ.get("JIRACLOUD_USEREMAIL")
itoken = os.environ.get("JIRACLOUD_TOKEN")
message= jiracloudApi.runjiracloudApi(api=iapi, method=imethod, url=iurl, useremail=iuseremail, token=itoken, json=ijson )
print(message)