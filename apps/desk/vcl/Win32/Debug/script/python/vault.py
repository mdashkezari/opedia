import dropbox

token = 'dO4RNV4OBNAAAAAAAAFyg3gxT_Wu3zsPPitxxcmLi0_cas-3GF6-vqM_rJ0ioe3o'
dbx = dropbox.Dropbox(token)
print dbx.users_get_current_account()

#dbx.files_upload()

for entry in dbx.files_list_folder('').entries:
    print(entry.name)


