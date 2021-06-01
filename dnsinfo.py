import argparse
import dns.resolver

parser = argparse.ArgumentParser()
parser.add_argument('-d' , '--domain', help='Provide Domain' , type=str)
parser.add_argument('-t' , '--type', help='Record Type' , type=str)
args = parser.parse_args()

domainName = args.domain
recordType = args.type

def headerPrint(msg):
    print()
    print(msg)
    print('-'*len(msg))
    print()


if domainName != None and  recordType != None: 
    resolver = dns.resolver.Resolver()
    if recordType == 'NS':
        msg = 'NameServer Records'
        headerPrint(msg)
        try:
            nameServers = resolver.query(domainName,'NS')
            for nameServer in nameServers:
                nameServer = str(nameServer)
                nameServerIps = resolver.query(nameServer,'A')
                for nameServerIp in nameServerIps:
                    print(nameServer,nameServerIp)
            print()
        except Exception as err:
            print('Error : ' , err)
            print('Usage : args -d DomainName')

    elif recordType == 'MX':
        msg = 'Mail Exchanger Records'
        headerPrint(msg)
        try:
                mail_Servers = resolver.query(domainName,'MX')
                for mail_Server in mail_Servers:
                    mta_Full_Details = mail_Server
                    mta_Name = str(mta_Full_Details).split()[-1]
                    mta_Ips = resolver.query(mta_Name,'A')
                    for mta_ip in mta_Ips:
                        print(mta_Full_Details,mta_ip)
                    print('>>')
        except Exception as err:
            print('Error : ' , err)
            print('Usage : args -d DomainName') 

    elif recordType == 'A':
        msg = 'Address Records'
        headerPrint(msg)
        try:
                hostIps = resolver.query(domainName,'A')
                for hostIp in hostIps:
                  print(hostIp)
                print()
        except Exception as err:
            print('Error : ' , err)
            print('Usage : args -d DomainName') 
    else:
        print('Unknown Record Type')
        print('Usage : args -d DomainName')

else:
    print('Usage : args -d DomainName')


