import requests
import threading
import time

def banAll(guild_id, members_id, bot_token):
    session = requests.Session()
    def start():
        r = session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{members_id}", headers={"Authorization": f"Bot {bot_token}"})
        if r.status_code == 429:
            time.sleep(r.json()['retry_after'])
            
    threading.Thread(target=start).start()

def deleteRoles(guild_id, roles_id, bot_token):
    session = requests.Session()
    def delete_role():
        while True:
            r = session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{roles_id}", headers={"Authorization": f"Bot {bot_token}"})
            if r.status_code == 429:
                time.sleep(r.json()['retry_after'])
            
    threading.Thread(target=delete_role).start()
    
def deleteChannels(channels_id, bot_token):
    session = requests.Session()
    def delete_chan():
        while True:
            r = session.delete(f"https://discord.com/api/v9/channels/{channels_id}", headers={"Authorization": f"Bot {bot_token}"})
            if r.status_code == 429:
                time.sleep(r.json()['retry_after'])
            
    threading.Thread(target=delete_chan).start()
    
def kickAll(guild_id, members_id, bot_token):
    session = requests.Session()
    def start():
        r = session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/members/{members_id}", headers={"Authorization": f"Bot {bot_token}"})
        if r.status_code == 429:
            time.sleep(r.json()['retry_after'])
            
    threading.Thread(target=start).start()

def createChan(guild_id, amount:int, channel_name, type_c, bot_token):
    if type_c == 'voice':
        json = {'name': channel_name, 'type': 2}
    else:
        json = {'name': channel_name, 'type': 0}
        
    def create_chan():
        session = requests.Session()
        r = session.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers={"Authorization": f"Bot {bot_token}"}, json=json)
        if r.status_code == 429:
            time.sleep(r.json()['retry_after'])
            
    for i in range(amount):
        threading.Thread(target=create_chan).start()

def createRole(guild_id, amount:int, role_name, bot_token):
    
    json = {'name': role_name}
    
        
    def create_role():
        session = requests.Session()
        r = session.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers={"Authorization": f"Bot {bot_token}"}, json=json)
        if r.status_code == 429:
            time.sleep(r.json()['retry_after'])
            
    for i in range(amount):
        threading.Thread(target=create_role).start()

def sendMeassges(channel_id, amount:int, message, bot_token):
    json = {'content': message}
    session = requests.Session()
    def mass_ping():
        r = session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers={"Authorization": f"Bot {bot_token}"}, json=json)
        if r.status_code == 429:
            time.sleep(r.json()['retry_after'])
            
    for i in range(amount):
        threading.Thread(target=mass_ping).start()