import requests
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS, ALL_REGIONS


def requests_ip_rotator_ex(n):
    """Run n requests using requests_ip_rotator to http://ip.jsontest.com/
    * http://ip.jsontest.com/ will return the Ip sent
    """

    # The site (without path) requests will be sent to.
    root_url ='http://ip.jsontest.com'
    # Create gateway object, initialise in AWS, and guarantees the shutdown
    with ApiGateway(site =root_url ,regions=["sa-east-1"]) as gateway:
        session = requests.Session()
        # The site given in mount must match the site passed in the ApiGateway constructor
        session.mount(root_url, gateway)

        # n requests
        for i in range(n):
            resp = session.get('http://ip.jsontest.com/')
            if resp.status_code == 200: 
                ip = resp.json().get('ip')
                print(f'Ip Sent: {ip}')
            else:
                raise Exception('Request Failed')


if __name__ == '__main__':
    # Execute 10 requests
    requests_ip_rotator_ex(10)