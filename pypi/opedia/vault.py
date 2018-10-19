
import os
import sys
sys.path.append(os.path.dirname(__file__))
import dropbox


def makedir(directory):
    	if not os.path.exists(directory):
		os.makedirs(directory)
	return

def vaultUpload(token, source, destination):
    dbx = dropbox.Dropbox(token)
    with open(source, 'rb') as f:
        dbx.files_upload(f.read(), destination)
    return


def listDBXContent(path):
    dbx = dropbox.Dropbox(token)
    f = open('.struc.txt', 'w')
    for entry in dbx.files_list_folder(path).entries:
        f.write(entry.name+'\n')
    f.close()    
    return        


def exportStruc(token):
    dbx = dropbox.Dropbox(token)
    makedir(vaultStrucDir)
    items=[]
    for entry in dbx.files_list_folder('', recursive=True).entries:
        items.append(entry.path_display)
        makedir(vaultStrucDir+entry.path_display)

    for item in items:
        path, dirs, files = os.walk(vaultStrucDir+item).next()
        count = len(files) + len(dirs)
        if item.split('/')[-1] in ['code', 'doc', 'nrt', 'rep'] and count<2000:
            for entry in dbx.files_list_folder(item, recursive=False).entries:            
                makedir(vaultStrucDir+entry.path_display)           
    return        

def refreshFolder(folder):
    dbx = dropbox.Dropbox(token)
    for entry in dbx.files_list_folder(folder, recursive=False).entries:            
        makedir(vaultStrucDir+entry.path_display)           
    
    return

vaultStrucDir = '.struc/'
token = 'dO4RNV4OBNAAAAAAAAFyg3gxT_Wu3zsPPitxxcmLi0_cas-3GF6-vqM_rJ0ioe3o'

if len(sys.argv)<2:
    exportStruc(token)

if len(sys.argv)>2:
    source = sys.argv[1]
    destination = sys.argv[2]
    vaultUpload(token, source, destination)
    refreshFolder(os.path.dirname(destination))
