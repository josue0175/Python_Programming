import re
import sys

def find_macs(live_macfile, inventory_macfile):
    my_macs = open(inventory_macfile).read().splitlines()
    mac = ''
    strToFind = re.compile(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', re.I)
    live_macfile = open(live_macfile)
    inventory_macfile = open(inventory_macfile)

    of_goodmac = open('respd_mac.txt', "w+b")
    of_badmac = open('nonrespd_mac.txt', "w+b")

    for line in live_macfile:
        results = re.search(strToFind, line)
        if results:
            mac = results.group()
        if mac in my_macs:
	    of_goodmac.write(mac + '\n')
        if mac not in my_macs:
	    of_badmac.write(mac + '\n')

    of_goodmac.close()
    of_badmac.close()


def main():
    if len(sys.argv) <= 1:
        print 'error: 2 args required'
        print '<live_macfile> <inventory_macfile>'
        sys.exit(1)
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    find_macs(filename1, filename2)

if __name__ == '__main__':
    main()
