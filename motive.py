import googlemaps
import pprint  # used to make shit easier to read
import time
import requests


def motive(address, address2, x):

    API_KEY = 'AIzaSyDlGREDN8stPvjn5ufbZdenr3p9WLEX2w0'

    gmap = googlemaps.Client('AIzaSyDlGREDN8stPvjn5ufbZdenr3p9WLEX2w0')

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' +
                            address+'&key=AIzaSyDlGREDN8stPvjn5ufbZdenr3p9WLEX2w0')
    response2 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' +
                             address2+'&key=AIzaSyDlGREDN8stPvjn5ufbZdenr3p9WLEX2w0')

    address_lat = response.json()['results'][0]['geometry']['location']['lat']
    address_lng = response.json()['results'][0]['geometry']['location']['lng']
    address2_lat = response2.json(
    )['results'][0]['geometry']['location']['lat']
    address2_lng = response2.json(
    )['results'][0]['geometry']['location']['lng']

    latitude = (address_lat + address2_lat)/2
    longitude = (address_lng + address2_lng)/2

    location = latitude, longitude

    key = API_KEY

    '''x = input('address_1')
    y = input('address_2')'''
    places_landmarks = []

    radius = 6000

    places_landmarks = gmap.places_nearby(location=(
        latitude, longitude), radius=radius, open_now=False, keyword=x.lower())['results']
    return places_landmarks
