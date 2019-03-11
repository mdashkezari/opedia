
import os
sys.path.append('../../config')
import config_vault as cfgv

outputdir = '/media/nrhagen/Drobo/OpediaVault/observation/remote/satellite/modisGridAtm/rep'
key = '7DE1AF06-4367-11E9-A7BA-A2D984A7CFCA'
wget_str = wget -A "*MYD08_M3*" -e robots=off -m -np -R .html,.tmp -nH --cut-dirs=3 "https://ladsweb.modaps.eosdis.nasa.gov/archive/NetCDF/L3_Monthly/V02/?process=ftpAsHttp&path=NetCDF%2fL3_Monthly%2fV02" --header "Authorization: Bearer ' + key + ' -P' + outputdir

def wget_grid_atmos(wget_str):
    os.system(wget_str)

def clean_cfgv():
    os.chdir(outputdir + '/V02')
    os.system('mv *.nc* ' + outputdir)
    os.system('rm -r ' + outputdir + '/V02/')

wget_grid_atmos()
clean_cfgv()
