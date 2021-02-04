import os

def disk_size(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for fileName in os.listdir(path):
            childPath = os.path.join(path, fileName)
            total+= disk_size(childPath)
    print('{0:<7}'.format(total),path)
    return total


disk_size('D:\Softwares')