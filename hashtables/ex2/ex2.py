class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # Make the array to store the tickets
    cache = {}
    # add in the tickets with the source as the key
    # and the destination as the value
    for i in tickets:
        cache[i.source] = i.destination

    # make the route to return later
    route = []

    # Start out with the first ticket which we know
    # has a source of none.
    current_ticket = cache["NONE"]
    for i in range(0, length):
        # for every item in the array, add the destination
        route.append(current_ticket)
        # then update the current ticket so the destination becomes
        # the key/source for the next ticket
        current_ticket = cache[current_ticket]
    # return the route in order
    return route
