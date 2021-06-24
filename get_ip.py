#from geoip import geolite2
import pycountry

def main(ip):
    import re
    import json
    from urllib.request import urlopen

    url = 'http://ipinfo.io/{0}/json'.format(ip)
    response = urlopen(url)
    data = json.load(response)
    country =  pycountry.countries.get(alpha_2=data['country']).name
    print(country)
    return country

    #match = geolite2.lookup(ip)
    #match is not None
    #match.country
    #match.continent
    #match.timezone
    #match.subdivisions
    #if match:
    #    country = match.country
    #    return pycountry.countries.get(alpha_2=country).name
    #else:
    #    return