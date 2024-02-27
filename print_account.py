from Pinterest import Pinterest
#from py3pin.Pinterest import Pinterest
import pickle
import random

pinterest = Pinterest(email='atticoarts@outlook.com',
                      password='hdb56rPr8yBLZqx',
                      username='atticoarts',
                      cred_root='/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/cred_root',
                      proxies={"http": "168.158.231.170:59101"}) #proxies={"http": "45.85.204.3:59101"}

with open("/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/all_prints.pkl", "rb") as f:
    fil = pickle.load(f)
current_pin = random.choice(fil)

boards = ["932385997793892268"]
board_id = random.choice(boards)

titles = ["Elegant Painting | Printable Vintage Art | Home Decor", "Elegant Art Prints for your Room | Home Decor"]
title = random.choice(titles)

describtions = ["Discover the nostalgic charm of our sweet collections of vintage printable art. Perfect for every room, these timeless artworks bring life into every corner, awakening emotions and creating a cozy vibe. #vintageart #homedecor #printablewallart #eartydecor #farmhousedecor #countryliving"]
describtion = random.choice(describtions)


pinterest.pin(image_url=f"https://pincontainer.blob.core.windows.net/artprints/{current_pin}.jpg", board_id=board_id, description=describtion)

fil.remove(current_pin)
with open("/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/all_prints.pkl", "wb") as f:
    pickle.dump(fil, f)
