import requests
import pook


# Use context
with pook.use():
    def on_match(request, mock):
        print('On match:', request, mock)

    pook.get('http://httpbin.org/ip',
             reply=403, response_type='json',
             response_headers={'pepe': 'lopez'},
             response_json={'error': 'not found'},
             callback=on_match)

    pook.get('http://httpbin.org/headers',
             reply=404, response_type='json',
             response_headers={'pepe': 'lopez'},
             response_json={'error': 'not found'},
             error=Exception('foo'),
             callback=on_match)

    res = requests.get('http://httpbin.org/ip')
    print('Status:', res.status_code)
    print('Headers:', res.headers)
    print('Body:', res.json())

    res = requests.get('http://httpbin.org/headers')
    print('Status:', res.status_code)
    print('Headers:', res.headers)
    print('Body:', res.json())

    print('Is done:', pook.isdone())
    print('Pending mocks:', pook.pending_mocks())
    print('Unmatched requests:', pook.unmatched_requests())