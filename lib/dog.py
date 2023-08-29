#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='mutt'):
        self.name = name
        self.breed = breed



Fido = Dog('Fido', 'Spitz')
Fido.name
Fido.breed


Snoopy = Dog('Snoopy')
