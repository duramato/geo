from geoip import geolite2
import pycountry

def main(ip):
    match = geolite2.lookup(ip)
    #match is not None
    #match.country
    #match.continent
    #match.timezone
    #match.subdivisions
    if match:
        country = match.country
        return pycountry.countries.get(alpha_2=country).name
    else:
        return