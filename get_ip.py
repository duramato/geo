#from geoip import geolite2
import pycountry

def main(ip):
    import re
    import json
    from urllib.request import urlopen

    import pygeoip
    gi = pygeoip.GeoIP('GeoLiteCity.dat')
    country = gi.country_name_by_addr(ip)
    code = gi.country_code_by_addr(ip)
    #print(country, "\n", code)
    return country, code

    url = 'https://ipwhois.app/json/{0}'.format(ip)
    response = urlopen(url)
    data = response.read()
    country = json.loads(data.decode("utf-8"))['country']
    code = json.loads(data.decode("utf-8"))['country_code']
    #print(country)
    return country, code

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