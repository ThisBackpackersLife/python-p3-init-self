#!/usr/bin/env python3
#import ipdb

class Dog:
        
    def __init__( self, name, breed = "Mutt" ):
        self.name = name
        #is_breed = breed if breed else "Mutt"
        self.breed = breed


joejoe = Dog( "Joe Joe", "Pitbull")

#stewie = Dog( "Stewie" )

#ipdb.set_trace()