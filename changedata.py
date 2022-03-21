import requests as rq
import pprint
url = "https://cvp.api.tatamotors/api/audit-service/get-alert-logs-data"
headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVZTNpTk5LcUNNMXQ2MjY2WGZBU2hieEN6anIyNlFGZ0U4TzJsN0lna3dJIn0.eyJqdGkiOiIyYTNiNDA0NC05Y2E5LTQ3OWItYmYyMy0wOWU0NjczNGJmYmQiLCJleHAiOjE2NDc0MDQ2NzksIm5iZiI6MCwiaWF0IjoxNjQ3MzE4Mjc5LCJpc3MiOiJodHRwczovL2N2cGF1dGguYXBpLnRhdGFtb3RvcnMvYXV0aC9yZWFsbXMvY3ZwIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImYyMDdkYTM0LTljYWMtNGZkYi04YzM0LTdiYzc1N2M5NzIzMyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImN2cC1mbXMiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiI5ZmZmMzEzYi00MjZmLTQ5MjgtYWM3OS0zZGE3NjY4ZGE1ZmMiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJSYWprdW1hciBHb3ZpbmRhcmFqYW4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJncmt0cmFuc3BvcnRzcHZ0bHRkQGdtYWlsLmNvbSIsImdpdmVuX25hbWUiOiJSYWprdW1hciIsImZhbWlseV9uYW1lIjoiR292aW5kYXJhamFuIiwiZW1haWwiOiJncmt0cmFuc3BvcnRzcHZ0bHRkQGdtYWlsLmNvbSJ9.CltAh-MZNe8p7kqL4-G8dPMPY-uN7C214vtu24P7uVvvV7F_E_M7HDVW3LW8P_gSHtwNmXDjjbyS3Ukjnn19na7b7SayIl5-prCqzbcgYJRZ8B4uSsaipW9nkVqvbVwALO5uJ_ChsRrfdiHyOjPXVh3qz68L1FMAKkPwjrIWERE1Hx5wdoAjmZw0YGjrNP01eAF73hXjff6Kez3yY3l321nyorYuPAYOIZRFj5oDl2-c"}
params = {"search_text":"","page_number":1,"sort":"","field_name":"event_date_time","filter_by":"vehicle","fleet_id":"U16081192830336153230","branch_id":"","alert_type":"","from_date":"2021-12-20T07:00:00.000Z","to_date":"2022-02-26T07:00:38.804703","mvp":"True"}
notification = rq.get(url=url,headers=headers,json=params).json()
pprint.pprint(notification)
# for data in notification['result']:
#     if (data['alert_log_type'] == 'Geofence'):
#         print(data['alert_log_name'])
#         break
#     else:
#         print(data['alert_log_name'])
#         continue