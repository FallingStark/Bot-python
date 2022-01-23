from pprint import pprint
from random import choice
import psutil
from pypresence import Presence
import time
import os

client_id = [
    "779738919129972786", #Regarde des animes [1]
    "934417298679271495", #League of legends [2]
]
os.system("cls")


number = int(input("Ton chiffre "))
number -= 1

RPC = Presence(client_id[number])
RPC.connect()

pprint(
    RPC.update(
        state="Waiting someone",
        details="in Lobby",
        large_image="pyke",
        small_image="saikikusuo",
        large_text="Pyke main",
        start=time.time(),
    )
)

while True:
    Timeout = 15
    end_time = time.time() + Timeout
    while time.time() < end_time:
        reponse = input('What is your input: ')
    if reponse == "stop":
        break
    print("Reloaded")