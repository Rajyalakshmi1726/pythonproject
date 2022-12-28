import win32api
availableDrivers=win32api.GetLogicalDriveStrings()
print(availableDrivers)
drivers=[drivestr for drivestr in availableDrivers.split('\000')if drivestr]
#drives=drives.split('\000')[:-1]
print(drivers)