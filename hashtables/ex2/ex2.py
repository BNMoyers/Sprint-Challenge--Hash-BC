#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    next_stop = hash_table_retrieve(hashtable, "NONE")
    while next_stop != "NONE":
        route.append(next_stop)
        next_stop = hash_table_retrieve(hashtable, next_stop)
            
    
    return route

