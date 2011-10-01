
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('surrogate.conf')

def get(var):
    return config.get('surrogate',var)

def items():
    return config.items('surrogate')

