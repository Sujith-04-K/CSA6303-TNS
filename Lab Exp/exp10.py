established = set()

def outbound(src, dst, sport, dport):
    connection = (src, dst, sport, dport)
    established.add(connection)
    print("Outbound connection allowed:", connection)

def inbound(src, dst, sport, dport):
    reverse = (dst, src, dport, sport)
    if reverse in established:
        print("Return traffic allowed")
    else:
        print("Unsolicited inbound traffic BLOCKED")

outbound("10.0.0.5", "203.0.113.10", 5000, 443)
inbound("203.0.113.10", "10.0.0.5", 443, 5000)
inbound("198.51.100.20", "10.0.0.5", 4444, 22)
