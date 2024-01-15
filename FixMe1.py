btr33z0r5-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/27/fixme1.py
--2024-01-15 21:25:17--  https://artifacts.picoctf.net/c/27/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.128, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                  100%[========================================>]     837  --.-KB/s    in 0s      

2024-01-15 21:25:17 (227 MB/s) - 'fixme1.py' saved [837/837]

btr33z0r5-picoctf@webshell:~$ python fixme1.py 
  File "/home/btr33z0r5-picoctf/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
btr33z0r5-picoctf@webshell:~$ nano fixme1.py 
btr33z0r5-picoctf@webshell:~$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_182342f7}