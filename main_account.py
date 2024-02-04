from Pinterest import Pinterest
#from py3pin.Pinterest import Pinterest
import pickle
import random

pinterest = Pinterest(email='basicdime@outlook.com',
                      password='rVz5mkZ4KpM6DXx',
                      username='basicdime',
                      cred_root='/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/cred_root',
                      proxies={"http": "103.52.226.184:59101"}) #proxies={"http": "45.85.204.3:59101"}

with open("/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/all_files.pkl", "rb") as f:
    fil = pickle.load(f)
current_pin = random.choice(fil)

boards = ["1020135821783407241", "1020135821783407242"]
board_id = random.choice(boards)

titles = ["The Best Part-Time Jobs from Home", "The Best Late Night Work From Home Jobs to earn money fast"]
title = random.choice(titles)

describtions = ["If you are looking to work late night from home,there are dozens of late-night work-from-home jobs you can choose from which are both flexible and makes high income  #sidejobs #workfromhome #earnmoneyfromhome",
               "Learn how to make money with these late-night/evening jobs from home: 34 ways to do so #sidejobs #workfromhome #earnmoneyfromhome"]
describtion = random.choice(describtions)

link = "https://basicdime.com/work-from-home/30-best-part-time-jobs-from-home/"
pinterest.pin(image_url=f"https://pincontainer.blob.core.windows.net/30nightjobs/{current_pin}.png", board_id=board_id, link=link, description=description)

fil.remove(current_pin)
with open("/home/nilslux/pinterest/pinterest-ZGTe44tfr6333jb-hksgD-DD/all_files.pkl", "wb") as f:
    pickle.dump(fil, f)
