
from re import S
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import json
import pprint
from os.path import exists
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
# golbal variables
api_key = 'RGAPI-9945c54d-8e0f-4e0f-929c-4abe631c6e74'
watcher = LolWatcher(api_key)
my_region = 'na1'


with open('summoners.json') as f:
    data = json.load(f)
keys = data.keys()
values = data.values()

summoner_ids = {'challenger' : [],
'grandmaster' : [],
'master' : [],
'diamond' : [],
'platinum' : [],
'gold' : [],
'silver' : [],
'bronze' : [],
'iron' : []}
if not exists('summoner_ids.json'):
    for key in summoner_ids.keys():
        summoners = data[key]
        for summoner in summoners:
            summoner_ids[key].append(watcher.summoner.by_name(my_region, summoner)['puuid'])
    with open('summoner_ids.json','w') as f:
        json.dump(summoner_ids,f)
else:
    with open('summoner_ids.json') as f:
        summoner_ids = json.load(f)

game_times = {'challenger' : [],
'grandmaster' : [],
'master' : [],
'diamond' : [],
'platinum' : [],
'gold' : [],
'silver' : [],
'bronze' : [],
'iron' : []}

match_list = {'challenger' : [],
'grandmaster' : [],
'master' : [],
'diamond' : [],
'platinum' : [],
'gold' : [],
'silver' : [],
'bronze' : [],
'iron' : []}
if not exists('match_list.json'):
    for key in match_list.keys():
        ids = summoner_ids[key]
        for id in ids:
            match_list[key].append(watcher.match.matchlist_by_puuid('americas',id,0,50,420))
    with open('match_list.json','w') as f:
        json.dump(match_list,f)
else:
    with open('match_list.json') as f:
        match_list = json.load(f)

if not exists('game_times.json'):
    for key in game_times.keys():
        match_ids = match_list[key]
        for ids in match_ids:
            for id in ids:
                print(id)
                game_times[key].append(watcher.match.by_id('americas', id)['info']['participants'][0]['timePlayed'])
    with open('game_times.json','w') as f:
        json.dump(game_times,f)
else:
    with open('game_times.json') as f:
        game_times = json.load(f)
positions = ['TOP','JUNGLE',"MIDDLE",'BOTTOM','UTILITY']
gepp = {
    'challenger' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'grandmaster' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'master' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'diamond' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'platinum' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'gold' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'silver' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'bronze' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    },
'iron' : {
        'TOP' : [],
        'JUNGLE' : [],
        'MIDDLE' : [],
        'BOTTOM' : [],
        'UTILITY' : []
    }
}
path = Path(r'matches')
files = list(path.glob('NA1_??????????.json'))
recorded_id = []
for file in files:
    file_str = str(file)
    recorded_id.append(file_str[file_str.find('NA1'):file_str.find('NA1')+14])



for key in game_times.keys():
    match_ids = match_list[key]
    for ids in match_ids:
        for id in ids:
            
            if id not in recorded_id:
                print(id)
                match = watcher.match.by_id('americas', id)
                match['tier'] = key
                with open(str(path)+'\\'+id+'.json','w') as f:
                                json.dump(match,f)
                                f.close()
for file in files:
    with open(file,encoding='ascii') as f:
        match = json.load(f)
        for i in range(10):
            tier = match['tier']
            for position in positions:
                if position == match['info']['participants'][i]['teamPosition']:
                    gold = match['info']['participants'][i]['goldEarned']
                    time = match['info']['participants'][i]['timePlayed']
                    gps = gold/time
                    gepp[tier][position].append(gps)
        f.close()
        
    
        

gps_avg = {
    'challenger' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'grandmaster' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'master' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'diamond' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'platinum' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'gold' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'silver' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'bronze' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    },
'iron' : {
        'TOP' : 0,
        'JUNGLE' : 0,
        'MIDDLE' : 0,
        'BOTTOM' : 0,
        'UTILITY' : 0
    }
}

for key in gps_avg.keys():
    for position in positions:
        total = 0
        for dict in gepp[key][position]:
            total += dict
        avg = total / len(gepp[key][position])
        gps_avg[key][position] = avg



game_time_avg = {'challenger' : 0,
'grandmaster' : 0,
'master' : 0,
'diamond' : 0,
'platinum' : 0,
'gold' : 0,
'silver' : 0,
'bronze' : 0,
'iron' : 0}
total = 0
for key in game_times.keys():
    for time in game_times[key]:
        total += time
    avg = round((total / len(game_times[key])))
    game_time_avg[key] = [avg,f'{avg//60}m {avg%60}s']
    
    total = 0
tiers = ['challenger', 'grandmaster', 'master', 'diamond', 'platinum', 'gold','silver','bronze','iron']
gpss = {}
# for tier in tiers:
#     print(tier + ": "+game_time_avg[tier][1])
for position in positions:
    print(position + ':\n')
    gpss[position]=[]
    for tier in tiers[::-1]:
        print('  '+ tier + ': '+str(gps_avg[tier][position]))
        gpss[position].append(gps_avg[tier][position])
    print('\n')

fig, ax = plt.subplots()  
plt.figure(1) 
for key in gpss.keys():
    plt.plot([item.upper() for item in tiers[::-1]],gpss[key],label = key)
plt.xticks(rotation=90)

plt.xlabel('Divisions')
plt.ylabel('Gold Per Second')
plt.title('GPS for different divisions')
plt.legend()
plt.tight_layout()
plt.figure(2)

game_time_avg_list = []
game_time_avg_listf = []
for tier in tiers[::-1]:
    game_time_avg_list.append(game_time_avg[tier][0])
    game_time_avg_listf.append(game_time_avg[tier][1])
plt.bar([item.upper() for item in tiers[::-1]],game_time_avg_list)
plt.xticks(rotation=90)
plt.xlabel('Divisions')
plt.ylabel('Game time')
plt.title('Average game time for different divisions')
# plt.yticks(game_time_avg_listf)
print(game_time_avg_list)
def minsecs(x,pos=None):
    return f'{int(x//60)}m {int(x%60)}s'
plt.ylim(1500,1850)
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(minsecs))
plt.legend()
plt.tight_layout()

plt.show()