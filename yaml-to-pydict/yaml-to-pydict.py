import yaml 
from rich import print as rprint

data = yaml.safe_load(open("raw_data.yaml"))
#print(data)
rprint(data["bgp"]["neighbors"][0])

