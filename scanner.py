import argparse 

parser  = argparse.ArgumentParser()

ports = [ '80' , '22' , '443']
parser.add_argument("-i" , dest="rHost",help="Provide Your IP for Scan.", metavar="")
parser.add_argument("-p" , dest="rPorts",help="Provide Your Ports for Scan.", metavar="" , nargs="+" , choices=ports)

args = parser.parse_args()

'''
print('Args :',args)
print('args.rHost :',args.rHost , 'type', type(args.rHost))
print('args.rPorts :',args.rPorts , 'type', type(args.rPorts))
'''

if args.rHost and args.rPorts:
    for port in args.rPorts:
        print('Sanning '+args.rHost+':'+port)
else:
    print('None')
