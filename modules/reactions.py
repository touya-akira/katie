def learnPython(phenny, input):
	phenny.say('I recommend: http://learnpythonthehardway.org/')
learnPython.rule = r'python?'
learnPython.priority = 'medium'

def vpn(phenny, input):
	phenny.say('Currently I can recommend two privacy vpn providers, '+input.nick+': Perfect Privacy (http://perfect-privacy.com) and ovpn (http://ovpn.to), ')
vpn.rule = r'vpn?'
vpn.priority = 'medium'

def dnsleaks(phenny, input):
	phenny.say('A DNS leak means that you are using a fixed nameserver (like the one from your provider) which may compromise your anonymity. Read about it here: http://www.dnsleaktest.com/what-is-a-dns-leak.php')
	phenny.say('You can test this on this website: http://www.dnsleaktest.com/ - to prevent DNS leaks when using TOR, read the following: https://trac.torproject.org/projects/tor/wiki/doc/PreventingDnsLeaksInTor')
dnsleaks.rule = r'dnsleaks?'
