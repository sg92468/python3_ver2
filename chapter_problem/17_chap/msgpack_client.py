from msgpackrpc import Address, Client

client = Client(Address("localhost", 6789))
num = 8
result = client.call('double', num)
print(f"Double {num} is {result}")