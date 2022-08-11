import requests
import csv

smsCsv = open('sms.csv', 'w', encoding='utf-8', newline='')
emailCsv = open('email.csv', 'w', encoding='utf-8', newline='')
bothCsv = open('both.csv', 'w', encoding='utf-8', newline='')
exceptionCsv = open('exception.csv', 'w', encoding='utf-8', newline='')

smsFile = csv.writer(smsCsv)
emailFile = csv.writer(emailCsv)
bothFile = csv.writer(bothCsv)
exceptionFile = csv.writer(exceptionCsv)

smsFile.writerow(["sms"])
emailFile.writerow(["email"])
bothFile.writerow(["both"])
exceptionFile.writerow(["exception"])

f = open('uuid.csv', 'r')
rdr = csv.reader(f)
for line in rdr:

    if line[0] == "uuid":
        continue

    headers = {
        'Authorization': 'KakaoAK 68b9adbb391aa466859ab39d50944d4d',
    }

    params = {
        'target_id_type': 'user_id',
        'target_id': line[0],
    }

    response = requests.get('https://kapi.kakao.com/v1/user/service/terms', params=params, headers=headers)
    json1 = response.json()

    if 'NotRegisteredUserException' in json1.__str__():
        print('NotRegisteredUserException')
        exceptionFile.writerow([line[0]])

    else:
        if 'sms' in json1["allowed_service_terms"].__str__():
            print("sms")
            smsFile.writerow([line[0]])

        if 'email' in json1["allowed_service_terms"].__str__():
            print("email")
            emailFile.writerow([line[0]])

        if 'email' in json1["allowed_service_terms"].__str__():
            if 'sms' in json1["allowed_service_terms"].__str__():
                print("both")
                bothFile.writerow([line[0]])

    print(json1)
    #
    # print(json1["allowed_service_terms"])

f.close()


smsCsv.close()
emailCsv.close()
bothCsv.close()
exceptionCsv.close()

# headers = {
#     'Authorization': 'KakaoAK 68b9adbb391aa466859ab39d50944d4d',
# }
#
# params = {
#     'target_id_type': 'user_id',
#     'target_id': 2140275718,
# }
#
# response = requests.get('https://kapi.kakao.com/v1/user/service/terms', params=params, headers=headers)
# json1 = response.json()
# if 'tag' in json1:
#     print(2140275718)
# if 'user_id' in json1:
#     print("userid")
# if 'sms' in json1["allowed_service_terms"].__str__():
#     print("sms")
# if 'ase' in json1["allowed_service_terms"].__str__():
#     print("ase")
# if 'email' in json1["allowed_service_terms"].__str__():
#     print("email")
# if 'private' in json1["allowed_service_terms"].__str__():
#     print("private")
# print(response)
# print(json1)
#
# print(json1["allowed_service_terms"])
