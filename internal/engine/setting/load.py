import yaml

path = 'config/config.yml'

def openConfig():
    with open(path, 'r') as f:
        cfg = yaml.safe_load(f)
    f.close()
    
    global coding
    coding = cfg['coding']
    
    global stdHeight
    stdHeight = cfg['stdHeight']
    
    global tcpPort  
    tcpPort = cfg['tcpPort']
    
    global serverHost
    serverHost = cfg['serverHost']
    
openConfig()