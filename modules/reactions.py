#!/usr/bin/python
def clients(phenny, input):
	phenny.say('There are several IRC clients for all operating systems. For Windows, we recommend hexchat (Free X-Chat Successor, http://hexchat.org). For Unix/Linux consider X-Chat (GUI) or irssi (console), both available in your repository. For Mac try XChat Aqua (http://xchataqua.github.com/)')
clients.rule = r'^clients\?'

def dnsleaks(phenny, input):
        phenny.say('A DNS leak means that you are using a fixed nameserver (like the one from your provider) which may compromise your anonymity. Read about it here: http://www.dnsleaktest.com/what-is-a-dns-leak.php')
        phenny.say('You can test this on this website: http://www.dnsleaktest.com/ - to prevent DNS leaks when using TOR, read the following: https://trac. torproject.org/projects/tor/wiki/doc/PreventingDnsLeaksInTor')
dnsleaks.rule = r'^dnsleaks\?'

def freevpn(phenny, input):
	phenny.say('Personally I would not trust any free VPN for the simple reason that if a VPN provider has no product for sale, chances are that they are selling YOU.')
freevpn.rule = r'^freevpn\?'

def hacking(phenny, input):
	phenny.say('How to Become a Hacker: http://www.catb.org/esr/faqs/hacker-howto.html')
hacking.rule = r'^hacking\?'

def i2p(phenny, input):
	phenny.say('I2P is an anonymous network, exposing a simple layer that applications can use to anonymously and securely send messages to each other http://www.i2p2.de/intro.html - http://www.i2p2.de/faq.html')
i2p.rule = r'^i2p\?'

def python(phenny, input):
	phenny.say('I recommend: http://learnpythonthehardway.org/')
python.rule = r'^python\?'
python.priority = 'medium'

def tor(phenny, input):
	phenny.say('Tor is a network of virtual tunnels that allows people and groups to improve their anonymity and security on the Internet. Read more here: https://www.torproject.org/about/overview.html.en and here https://www.torproject.org/docs/documentation.html.en')
tor.rule = r'^tor\?'

def vm(phenny, input):
	phenny.say('Virtual machines allow you to run one operating system emulated within another operating system. Your primary OS can be Windows 7 64-bit, for example, but with enough memory and processing power, you can run Ubuntu and OS X side-by-side within it. More information: http://lifehacker.com/5714966/five-best-virtual-machine-applications')
vm.rule = r'^vm\?'

def vpn(phenny, input):
    phenny.say('Currently I can recommend two privacy vpn providers, '+ input.nick +': Perfect Privacy (http://perfect-privacy.com) and ovpn (http://ovpn.to)')
vpn.rule = r'^vpn\?'
vpn.priority = 'medium'


#topics


def topics(phenny, input):
    phenny.say('Currently I can advise about the following topics: clients, freevpn, dnsleaks, hacking, i2p, python, vm, vpn and tor. Use "topic?" to get specific info on a topic.')
topics.rule = r'^topics\?'


#generic stuff

def Logbot(phenny, input):
	phenny.say('lol logbots <3')
Logbot.rule = r'.*logbot.*'

#punishment

def troutpatro(phenny, input):
	phenny.write(['kick',input.sender,input.nick,'Trout slaps are incredibly lame. [Troutpatrol]'])
#	phenny.say('!kick '+ input.nick + ' Trout slaps are incredibly lame. [Troutpatrol]')
troutpatro.rule = r'.*slaps.*trout'
