import bcrypt

simple_string = "Hello World" # unicode format

generated_solt = bcrypt.gensalt()
# bcrypt.hashpw(simple_string, generated_solt) # got error because 1st parameter is normal python string, it should be encoded with "utf-8"

simple_string_bytes = simple_string.encode("utf-8") # convert it to bytes (we can use ascii, latin-1, utf-16 etc in here)
# utf-8 is best choice, it can support all type of language (Bangla, English, Chaina, Emoji etc)
# print(type(simple_string_bytes)) <----------> <class 'bytes'>

hashed = bcrypt.hashpw(simple_string_bytes, generated_solt)
print(hashed)
