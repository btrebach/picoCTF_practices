btr33z0r5-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/22/convertme.py
--2024-01-15 21:22:30--  https://artifacts.picoctf.net/c/22/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.128, 3.160.22.43, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1.2K) [application/octet-stream]
Saving to: 'convertme.py'

convertme.py               100%[========================================>]   1.16K  --.-KB/s    in 0s      

2024-01-15 21:22:30 (353 MB/s) - 'convertme.py' saved [1189/1189]

btr33z0r5-picoctf@webshell:~$ python convertme.py
If 83 is in decimal base, what is it in binary base?
Answer: 01010011
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}