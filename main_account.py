from Pinterest import Pinterest
#from py3pin.Pinterest import Pinterest
import pickle
import random

pinterest = Pinterest(email='theredditwonda@gmail.com',
                      password='Baum96?!',
                      username='coaxonstudios',
                      cred_root='/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/cred_root') #proxies={"http": "45.85.204.3:59101"}

with open("/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/all_files.pkl", "rb") as f:
    fil = pickle.load(f)
current_pin = random.choice(fil)

pinterest.pin(image_url=f"https://pincontainer.blob.core.windows.net/30nightjobs/{current_pin}.png", board_id="928304610631143129", link="basicdime.com")

fil.remove(current_pin)
with open("/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/all_files.pkl", "wb") as f:
    pickle.dump(fil, f)
