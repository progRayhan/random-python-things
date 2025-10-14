import pygit2
    
git_token = "KJJFKJGVFDJHJFOLFGJDFJKFGIUFIUFUJDUHFCIKGOIUG"

url='https://github.com/progRayhan/Lost2Found.git'
path='/home/upay/Desktop/Practice/random-python-things/test'

credentials = pygit2.UserPass("x-access-token", git_token)
callbacks = pygit2.RemoteCallbacks(credentials=credentials)
repo = pygit2.clone_repository(url, path, callbacks=callbacks)
print("Cloned:")
