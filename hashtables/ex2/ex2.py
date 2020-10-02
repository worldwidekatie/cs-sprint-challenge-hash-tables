class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        
def reconstruct_trip(tickets, length):
    cache = {}
    for i in tickets:
        cache[i.source] = i.destination

    route = []
    current_ticket = cache["NONE"]
    for i in range(0, length):
        route.append(current_ticket)
        current_ticket = cache[current_ticket]
    return route
