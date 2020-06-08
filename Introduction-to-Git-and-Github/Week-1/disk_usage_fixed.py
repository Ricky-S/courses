import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    '''return true if there is enough free disk space, else false'''
    du = shutil.disk_usage(disk)
    percent_free= 100*du.free/du.total
    gigabytes_free = du.free/2**30
    print('gigabytes', percent_free,gigabytes_free, min_percent,min_absolute)
    if percent_free<min_percent or gigabytes_free < min_absolute:
        return False
    return True

if not check_disk_usage('/',2, 10):
    print('error not enough space')
    sys.exit(1)

print('everything ok')
sys.exit(0)