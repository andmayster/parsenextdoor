import requests
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query, value):
    cursor = connection.cursor(buffered=True)

    try:
        cursor.execute(query, value)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print("The error", e, "occured")


def execute_fetch(connection, query, value):
    cursor = connection.cursor(buffered=True)
    result = None
    try:
        cursor.execute(query, value)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("The error", e, "occured")


connection = create_connection("192.168.64.3", "andrys", "12345677", "db_test")


def main():



    try:
        name_suite = input()
        business = name_suite.split('/')[4]

        header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",\
                  'Accept': "*/*", 'Accept-Language': "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", 'Referer': name_suite,\
                  'content-type': "application/json",
                  'X-CSRFTOKEN': "WglJlcfOCxih5DtYuekXvl0yWWmuxvglTRLGgfERRumOs9SrhtYdcYRu2poLsbyA",\
                  'sentry-trace': "3eca194da73a4334b88453696b353054-992ba15da50e3d97-0",
                  'Origin': "https://nextdoor.com",\
                  'Connection': "keep-alive", 'Cookie': "csrftoken=oHmmc4X3vch3HXPvQK8bOI1BghA6jAPDliMj77m6K9lA4teYDZMrvlSxmKCneg7S; \
             WE=e2a3e29d-c623-44c6-9547-fdfff29ef5da201218; flaskTrackReferrer=1CAA9E19-E644-360B-6C74-9FA8603A74F4; \
        _gcl_au=1.1.1563973299.1608293680; _ga_L2ES4MTTT0=GS1.1.1608589497.4.0.1608589497.60; _ga=GA1.1.448582989.1608293681;\
         IR_gbd=nextdoor.com; IR_11953=1608585258199%7C0%7C1608585236537%7C%7C; __pdst=b70eb4a58b5042e8b9fa4b446702541b;\
          _scid=5a2908c3-2c52-4df1-86b3-26b0f14a0abe; _sctr=1|1608242400000; _fbp=fb.1.1608293682636.1101760507;\
           __hstc=1713326.c5622de51e58a778646690ff16d405b7.1608293683792.1608559022785.1608585239444.3;\
            hubspotutk=c5622de51e58a778646690ff16d405b7; __hssrc=1; __ssid=6c09bf4bae9580c302d8e837c0e3964;\
             s=3rvq6nzy2gl1hu3sgjesnqxvdjn2l51g; __utma=260061842.448582989.1608293681.1608585246.1608589500.3;\
              __utmc=260061842; __utmz=260061842.1608294381.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);\
        _gid=GA1.2.1729320958.1608559023; _uetsid=64ed9d20439411eb8a150f474f5df4af; _uetvid=9aca5110412a11eb9eaecb9e16cdc9c6;\
         _dd_s=logs=1&id=b4f980b2-25b9-4ac4-88be-48d27eae9599&created=1608589458524&expire=1608590406516&rum=2;\
          WERC=f2dc0a91-a9f9-441c-b998-9c5b961b2cdf2012211608589497; __utmb=260061842.1.10.1608589500; __utmt=1", \
                  'Pragma': "no-cache", 'Cache-Control': "no-cache"}

        json = {"operationName": "businessProfile", "variables": {"slug": business, "startDate": "2020-12-22", \
                                                                  "endDate": "2020-12-28", "desktopMapWidth": 279,
                                                                  "desktopMapHeight": 217, "tabletMapWidth": 267, \
                                                                  "tabletMapHeight": 267, "mobileMapWidth": 400,
                                                                  "mobileMapHeight": 267},
                "extensions": {"persistedQuery": \
                                   {"version": 1,
                                    "sha256Hash": "10c609b1aa297f2e7ea06d218a54c70d9d0a1b2c4367d88fb7d715c1e6057c16"}}}

        r = requests.post('https://nextdoor.com/api/gql/businessProfile?', headers=header, json=json)
        var = r.json()
        id_business = var['data']['business']['id']
        name_business = var['data']['business']['name']
        address_business = var['data']['business']['address']['formatted']
        phone_business = var['data']['business']['phoneNumber']
        website_business = var['data']['business']['websiteUrl']
        topics_business = var['data']['business']['topics']
        category_business = []
        for top in topics_business:
            category_business.append(top['name'])

        sorted_category = ' | '.join(category_business)

        proverka = "SELECT id_ FROM nextdoor WHERE id_ = %s"
        check = execute_fetch(connection, proverka, [id_business])

        if check == []:
            add_data = "INSERT INTO nextdoor (id_, name_, address, phone, website, category) VALUES (%s, %s,%s,%s,%s,%s)"
            value = [id_business, name_business, address_business, phone_business, website_business, sorted_category]
            execute_query(connection, add_data, value)
        else:
            print(f"This ({name_business}) business already exists")

    except:
        print("invalid data format")

    # name_suite = 'https://nextdoor.com/pages/cheddars-scratch-kitchen-thornton-co/'
    # business = name_suite.split('/')[4]
    # print(business) распечатать весь жсон


if __name__ == '__main__':
    main()