import os
import sys
import time
import requests
os.system('clear')
os.system('rm -rf list.txt')
os.system('id -u > list.txt')
uidd = open('list.txt', 'r')
for j in uidd:
    sp = j.split()

def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\n\n\x1b[37;1mYour ID : "+id) 
  try: 
    httpCaht = requests.get("https://github.com/kakacoder21/nkl/blob/main/hama.txt").text 
    if id in httpCaht: 
      print("\033[92mYOUR ID IS ACTIVE.........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[91mID ACTIVE NYA  Bo Active KRdn Nama Bnera La snap im_halo0\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print logo
     chk() 
    
chk()

os.system("clear")
os.system("xdg-open https://2no.co/2quNd6")    



logo = """



   ___    __   ___  
  / _ \  / /  / _ \ 
 | (_) |/ /_ | (_) |
  \__, | '_ \ > _ < 
    / /| (_) | (_) |
   /_/  \___/ \___/ 
                    
                    



-----------------------------------------------------------------------------------------------
\033[1;91m
\033[1;92m
\033[1;92mTelegram :@i4m_mrx
\033[1;92mTelegram Chanal:@staferor404
\033[1;96m
\033[1;92mAM Tooal Nrxi $0
\033[1;96m
\033[1;92m

"""

print logo
print '         1-Hacki camera'
print '         2-report fb'
print '         3-Hacki karti korak'
print '\t 4-dabazandy videoy fb '
print '         5-crack twitar'
print '         6-crack insta'
print '         7-report insta and tik tok'
print '         8-tlgram'
print '         0-ExiT'
im = raw_input('Halbzhera Dlm >>!')
if im == '1':
    import os
    os.system("clear")
    os.system("git clone https://github.com/Halo-404/Halo")
    os.system("python3 Halo/Halo404.py")
if im == '2':
    import os
    os.system("clear")
    os.system("git clone https://github.com/halocrak/re.git")    
    os.system("python2 re/404.py")
if im == '3':
    import os
    os.system("clear")
    os.system("git clone https://github.com/halocrak/korak.git")    
    os.system("python korak/korak.py")
elif im == '4':
    import os
    os.system("git clone https://github.com/halocrak/fb.git")
    os.system('php fb/fb.php') 
if im == '5':
    import os
    os.system("clear")
    os.system("git clone https://github.com/halocrak/kurd")    
    os.system("python kurd/kurd.py")
if im == '6':
    import os
    os.system("clear")
    os.system("git clone https://github.com/halocrak/cok")    
    os.system("python cok/cok.py")
if im == '7':
    import os
    os.system("clear")
    os.system("git clone https://github.com/halocrak/staf")    
    os.system("python staf/stafwa7sh.py")
if im == '8':
    import os
    os.system("clear")
    os.system("xdg-open https://t.me/i4m_mrx")    
    sys.exit()

