import requests
import os
import re
import time
import json
from datetime import datetime


notify_command = '''
    osascript -e 'display notification "CVS scraper notification" with title "Scraper Alert"' 
  '''
def requestCVSApi():
  cookies = {
      'akavpau_www_cvs_com_minuteclinic': '1598292717~id=2075adb189d1d61c70c48caea8ebe738',
      'akavpau_www_cvs_com_general': '1598295893~id=4e8c99a28f047011e75603d20df4e85b',
      'acctdel_v1': 'on',
      'adh_new_ps': 'on',
      'adh_ps_refill': 'on',
      'buynow': 'off',
      'db-show-allrx': 'on',
      'disable-app-dynamics': 'on',
      'disable-sac': 'on',
      'dpp_cdc': 'off',
      'dpp_drug_dir': 'off',
      'dpp_sft': 'off',
      'getcust_elastic': 'on',
      'echome_lean6': 'on',
      'enable_imz': 'on',
      'gbi_cvs_coupons': 'true',
      'ice-phr-offer': 'off',
      'v3redirecton': 'false',
      'mc_cloud_service': 'on',
      'mc_hl7': 'on',
      'mc_rio_locator2': 'on',
      'mdpguest': 'on',
      'memberlite': 'on',
      'pbmplaceorder': 'off',
      'pbmrxhistory': 'on',
      'rxdanshownba': 'off',
      'rxdfixie': 'on',
      'rxd_bnr': 'on',
      'rxd_dot_bnr': 'off',
      'rxdpromo': 'on',
      'rxduan': 'on',
      'rxlite': 'on',
      'rxlitelob': 'off',
      'rxm_demo_hide_LN': 'off',
      'rxm_phdob_hide_LN': 'on',
      'rxm_rx_challenge': 'on',
      's2c_rewardstracker': 'on',
      's2cHero_lean6': 'on',
      'sft_mfr_new': 'on',
      'v2-dash-redirection': 'on',
      'dfl': 'on',
      'akavpau_vp_www_cvs_com_minuteclinic_covid19': '1606686968~id=6fff3b489a0bd69cbcdb68fb41d2a845',
      'pe': 'p1',
      'BVImplall_route': '3006_3_0',
      'DG_SID': '69.138.14.251:zkVoL4x3SVNA8hjj0CEj7y1sABx4s7A1KVexQOTNcvo',
      'favorite_store': '2274/38.8838/-77.0932/Arlington/VA',
      'enable_imz_cvd': 'off',
      'akavpau_vp_www_cvs_com_shop': '1610900342~id=4022a0b159b1c3ba8ba3d3e0d958a812',
      'akavpau_vp_www_cvs_com_general': '1610900351~id=ed9c8a3c101be4b7918f170d270f8939',
      'AMCVS_06660D1556E030D17F000101%40AdobeOrg': '1',
      'adh_ps_pickup': 'on',
      'sab_displayads': 'on',
      'dashboard_v1': 'off',
      'enable_imz_reschedule_instore': 'off',
      'enable_imz_reschedule_clinic': 'off',
      'mc_home_new': 'off1',
      'mc_videovisit': 'on',
      'pivotal_forgot_password': 'off-p0',
      'pivotal_sso': 'off-p0',
      'ps': 'on',
      'rxm': 'on',
      'rxm_phone_dob': 'off-p1',
      's2c_akamaidigitizecoupon': 'on',
      's2c_beautyclub': 'off-p0',
      's2c_digitizecoupon': 'on',
      's2c_dmenrollment': 'off-p0',
      's2c_herotimer': 'off-p0',
      's2c_newcard': 'off-p0',
      's2c_papercoupon': 'on',
      's2c_persistEcCookie': 'on',
      'sftg': 'on',
      'show_exception_status': 'on',
      '_group1': 'quantum',
      'gbi_visitorId': 'ckm3jhjlj00013f7qr0v9scih',
      'JSESSIONID': 'N1JfpU4fSBfnoN5oWoS6SQTDz-nS9N6-cwlaqS7c.commerce_1304',
      'pauth_v1': 'on',
      'echomeln6': 'off-p2',
      'flipp2': 'on',
      'mc_ui_ssr': 'off-p0',
      'refill_chkbox_remove': 'off-p0',
      's2c_rewardstrackerbctile': 'on',
      's2c_rewardstrackerbctenpercent': 'on',
      's2c_rewardstrackerqebtile': 'on',
      's2c_smsenrollment': 'on',
      'CVPF': 'CT-2',
      'akavpau_vp_www_cvs_com_vaccine_covid19': '1617629366~id=13923952ec6a9e78ceb2adde82ec9965',
      'bm_sz': '2A442ECC6F92AA72B07BDF667392344D~YAAQd6omF4AA1Hd4AQAAUCIwogtM7ARh+JEncOH11Nw/ZzxhUCkO28brF6LWCexRJlNq/Zjk1tc/8EQvRb7eqmCeqkpVcCMpshGxHGR/rO/RYLQCkRnirMFKLFF5lKJMetzTFyUIsQKrTHTy1H15DZet+AcEWzDbOBe4j3TSoq//cNvnp5Go0etathdy',
      'AMCV_06660D1556E030D17F000101%40AdobeOrg': '-330454231%7CMCIDTS%7C18723%7CMCMID%7C04237398351295515122708889119945267616%7CMCAID%7CNONE%7CMCOPTOUT-1617635968s%7CNONE%7CvVersion%7C3.1.2',
      'ak_bmsc': 'C5C090C8FE7325819D477978D974F8AAACE8134C1E7B0000E43C6B6050C2C93F~plo1XTfNuxAM4ycB0QIwW/xyWIoE1nl1v8SFsLlrcX/mjflhL4gf3yqNPMBKxlHiFLiiAu+xb3zZxcVJiyOWwnzjwz8V1rJp1uQfFfOwYTen2hEhOjFnwKRJDoRGQgY1ubA5F0q0GJzRQsQQuHy5+POSWTS4yJ4kgynluPUexVEhyWyGGcrscEuzmZRajXWF7CB+yns3xWMs56gAt2oOhWfI7snlqtc6xQ5mqa3KIf6mk=',
      'bm_sv': '1D6466C69B3486FDA2BDE9F817877F29~9ePCmu51d1fAjjiyCzO1puce1E8WYWD2ilm1rqu7wB6BKTOgkew0YgGFgbHBPnEel0pIQGS8mv3OU3PqFJDnt6cfBz7K389kOeJTeNh1HdLHDdYdiPvc4R4KxRIlt8PeyNbkyNlFUmNPmpDJHjluvA==',
      '_abck': '2EC8AB5DBB9903167684C63AD5FFAECA~0~YAAQTBPorCZfo3V4AQAAHmbsogWYiaR1uJbzaP2IVUqUsh1gIL1oBEJfbphyO82yZ9eA7fcSj0vRS0zQlKWO73Ak8zGHff5dlPODBntY8OEYuS+V197tkHB2SBh6XZHtN35EFIubE94R4pDBuMN8ymJwTPokATUjeGGANsvDBdPEfPxPdnwWozrz9Seflw4/4EqgMSleQvvN3SZ2SHzmSi9UgDnpxZ37sctwCd4qG6i2Hy5PvpqKIz7J/P+GjcRwgbi39E3NdslCv4mvKevCw/JaSgTzDMQv1agjtpcEscZhqpZq13AbBEAtDnDInJF7IvssMniCN2ug2H4BWGoQXH2KFQyToXQngxK58IVmpesiHQdtKpF2EFmxfuAUdORQxvBRPHcLbcvsL5kkFzmGB0HEMrQ0~-1~||-1||~-1',
  }

  headers = {
      'authority': 'www.cvs.com',
      'accept': 'application/json',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
      'content-type': 'application/json',
      'sec-gpc': '1',
      'origin': 'https://www.cvs.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select',
      'accept-language': 'en-US,en;q=0.9',
  }
  search = '02139'

  data = '{"requestMetaData":{"appName":"CVS_WEB","lineOfBusiness":"RETAIL","channelName":"WEB","deviceType":"DESKTOP","deviceToken":"7777","apiKey":"a2ff75c6-2da7-4299-929d-d670d827ab4a","source":"ICE_WEB","securityType":"apiKey","responseFormat":"JSON","type":"cn-dep"},"requestPayloadData":{"selectedImmunization":["CVD"],"distanceInMiles":35,"imzData":[{"imzType":"CVD","ndc":["59267100002","59267100003","59676058015","80777027399"],"allocationType":"1"}],"searchCriteria":{"addressLine":"Boston, MA"}}}'

  response = requests.post('https://www.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores', headers=headers, cookies=cookies, data=data)

  try:
    return json.loads(response.text)
  except Exception as e:
    print(e)
    return {}
  
count = 0
while(True):
  api_output = requestCVSApi()
  resp =  api_output['responseMetaData']
  #print(resp)
  if resp:
    if resp['statusDesc'] == 'No stores with immunizations found':
      print("No Space", count)
    else: 
      print("Possibly Space?")
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      print("Time =", current_time)
      print(api_output)
      os.system('say "CVS Appointment Alert"')
      os.system(notify_command)
  time.sleep(5)
  count += 1