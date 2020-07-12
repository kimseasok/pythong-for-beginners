first = 'John'
last = 'Smith'
message = first + '[' + last + '] is a coder'

msg = "%s [%s] is a coder" % (last, first)

msg = f'{first} {last}'

# msg = F"Hello {last}."

print(msg)

print(msg.upper())

print(msg)

# get string index

print(msg.find('J'))

# replace

print(msg.replace('John', 'Jane'))

# check string 

print('John' in msg)

print(len(msg))
