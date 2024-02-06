#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    joe = Visitor("Joe")
    pam = Visitor("Pam")

    park = NationalPark("Yellowstone")


    v1 = Trip(joe, park, "02-01-2009", "20-02-0892")
    v2 = Trip(pam, park, "02-01-2009", "20-02-0892")
    v3 = Trip(joe, park, "02-01-2009", "20-02-0892")
    park.best_visitor()


    # ipdb.set_trace()
