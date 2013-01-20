def dnsleaks(phenny, input):
        phenny.say('A DNS leak means that you are using a fixed nameserver      (like the one from your provider) which may compromise your anonymity. Read     about it here: http://www.dnsleaktest.com/what-is-a-dns-leak.php')
        phenny.say('You can test this on this website: http://www.dnsleaktest.  com/ - to prevent DNS leaks when using TOR, read the following: https://trac.   torproject.org/projects/tor/wiki/doc/PreventingDnsLeaksInTor')
dnsleaks.rule = r'dnsleaks?'

def hacking(phenny, input):
        phenny.say('How to Become a Hacker: http://www.catb.org/esr/faqs/hacker-howto.html')
hacking.rule = r'^hacking\?'

def i2p(phenny, input):
	phenny.say('I2P is an anonymous network, exposing a simple layer that applications can use to anonymously and securely send messages to each other. http://www.i2p2.de/intro.html - http://www.i2p2.de/faq.html')
i2p.rule = r'^i2p\?'

def python(phenny, input):
        phenny.say('I recommend: http://learnpythonthehardway.org/')
learnPython.rule = r'^python\?'
learnPython.priority = 'medium'

def topics(phenny, input):
        phenny.say('Currently I can advise about the following topics: dnsleaks, hacking, i2p, python, vpn and tor.')
topics.rule = "^topics\?"

def tor(phenny, input):
	phenny.say('Tor is a network of virtual tunnels that allows people and groups to improve their anonymity and security on the Internet. Read more here: https://www.torproject.org/about/overview.html.en and here https://www.torproject.org/docs/documentation.html.en')
tor.rule = r'^tor\?'

def vpn(phenny, input):
        phenny.say('Currently I can recommend two privacy vpn providers, '+     input.nick+': Perfect Privacy (http://perfect-privacy.com) and ovpn (http://    ovpn.to), ')
vpn.rule = r'^vpn\?'
vpn.priority = 'medium'
