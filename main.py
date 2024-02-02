
from Pinterest import Pinterest

pinterest = Pinterest(email='theredditwonda@gmail.com',
                      password='Baum96?!',
                      username='coaxonstudios',
                      cred_root='cred_root')
pinterest.login()



pinterest.pin(image_url="https://pincontainer.blob.core.windows.net/30nightjobs/1.png", board_id="928304610631143129", link="basicdime.com")

print("finished")
