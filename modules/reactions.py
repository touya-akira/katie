def learnPython(phenny, input):
	phenny.say('I recommend: http://learnpythonthehardway.org/')
learnPython.rule = r'python?'
learnPython.priority = 'medium'

def vpn(phenny, input):
	phenny.say('Currently I can recommend two privacy vpn providers, '+input.nick+': Perfect Privacy (http://perfect-privacy.com) and ovpn (http://ovpn.to), ')
vpn.rule = r'vpn?'
vpn.priority = 'medium'
