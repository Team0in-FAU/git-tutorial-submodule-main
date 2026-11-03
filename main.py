#!/usr/bin/env python3

from names.names import *
from contacts.contacts import *

print("I know these names:")

for name in get_names():
    print("- {}".format(create_contact(name)))
