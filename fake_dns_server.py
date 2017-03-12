from dnslib import *
from dnslib import server

local_addr = '0.0.0.0'
local_port = 53

class SpecialResolver:
    def resolve(self, request, handler):
        d = request.reply()
        q = request.get_q()
        q_name = str(q.qname)

        d.add_answer(*RR.fromZone(q_name + " 60 A 172.16.27.130"))
        return d

r = SpecialResolver()
s = server.DNSServer(r, port=local_port, address=local_addr)
s.start_thread()

while True:
	pass
