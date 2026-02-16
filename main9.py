import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

data = input ("Enter data to send :")
hash_value = generate_hash (data)

print("Generated Hash",hash_value)

recieved_data = input ("Enter recieved data :")
recieved_hash = generate_hash (recieved_data )

if recieved_hash == hash_value :
    print("Integrity Verified : Data not modified")

else :
    print ("Integrity Failed : Data Modified ")

