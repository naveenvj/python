import  json
import  requests
import subprocess

subprocess.call('clear',shell=True)
msg = 'country code finder'
print()
print(' ',msg.upper())
print(' ','-' * len(msg))
print()

lookup_ip = input(' Enter Your Ip Address :: ')
lookup_string = 'https://freegeoip.net/json/'+lookup_ip

try:
    reply = requests.get(lookup_string)
    geodata= json.loads(reply.text)
    print(' Country Is ::' , geodata['country_code'])

except:
   print(' Unable to Fetch', lookup_string)

