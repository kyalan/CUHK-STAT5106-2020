# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:49:45 2019

@author: KY
"""

def getGeojs(address, verbose=False):

    import urllib.request, urllib.parse, urllib.error
    import json
    import ssl
    
#    Reference: https://nominatim.org/release-docs/develop/api/Search/
    serviceurl = 'https://nominatim.openstreetmap.org/'

    if len(address) < 1: 
        print('==== Failure To Retrieve ====')
        print('Address is None Value.')
        return {}        

    parms = {}
    parms['q'] = address
    parms['addressdetails'] = 1
    parms['country'] = 'Hong Kong'
    parms['format'] = 'json'
    parms['limit'] = '1'
    url = serviceurl + '?' + urllib.parse.urlencode(parms)

    data = []
    if verbose: print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    if verbose: print('Status', uh.status)
    if uh.status==200:  data = uh.read().decode()
    if verbose: print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)[0]
    except:
        js = None

    if not js:
        print('==== Failure To Retrieve ====')
        print(data)
        return {}

    return js

def getGeojs_route(address_from, address_to, verbose=False):
    
    # Please code :)
    
    return None
