import requests
import datetime
import notify2

global available
available = False

def id_catcher(name, region, STATE_ID):
    name = name.lower()
    if region == 'state':
        URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        response = requests.get(URL, headers = headers)
        if response.ok:
            resp_json = response.json()
            for _ in resp_json["states"]:
                if name == _["state_name"].lower():
                    return _["state_id"]
    elif region == "district":
        URL = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{STATE_ID}"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        response = requests.get(URL, headers = headers)
        if response.ok:
            resp_json = response.json()
            for _ in resp_json["districts"]:
                if name == _["district_name"].lower():
                    return _["district_id"]

def main(DIST_ID, age):

    available = False
    print_flag = 'Y'
    numdays = 5
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]

    for date in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(DIST_ID, date)
        headers = {'user-agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        response = requests.get(URL, headers = headers)
        if response.ok:
            resp_json = response.json()
            flag = False
    #         print(resp_json)
            if resp_json["sessions"]:
                if(print_flag=='y' or print_flag=='Y'):
                    for session in resp_json["sessions"]:
                        if session["min_age_limit"] <= age and int(session["available_capacity"]) > 0:
                            available = True
                            notify2.init("Cowin Update")
                            n = notify2.Notification("Cowin slots available at {}!".format(session["name"]))
                            n.set_urgency(notify2.URGENCY_CRITICAL)
    #                         n.set_timeout(10000)
                            n.show()
                            print("Available on: {}".format(date))
                            print("\t", session["name"])
                            print("\t", session["block_name"])
                            print("\t Price: ", session["fee_type"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            if(session["vaccine"] != ''):
                                print("\t Vaccine: ", session["vaccine"])
                            print("\n\n")
                    else:
                        if not available:
                            print(f"No available slots on {date}")
                        
            else:
                print(f"No slots are open for {date} yet")
                
        else:
            print("Response not ok")
