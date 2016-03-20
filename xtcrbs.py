import os
##Config Section
d = 'C:\\Users\\xtcrunturned\\Desktop\\rocketservers\\Servers\\'

ignore = ["25466"]

##Code Section
x = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
i = 0
for item in x:
    for i in ignore:
        if i not in item:
            os.system('copy Kits.dll /Y "%s\\Rocket\\Plugins\\Kits.dll"'%item)
            os.system('copy RocketMod_TPA.configuration.xml /Y "%s\\Rocket\\Plugins\\RocketMod_TPA\\RocketMod_TPA.configuration.xml"'%item)
            os.system('copy MessageAnnouncer.configuration.xml /Y "%s\\Rocket\\Plugins\\MessageAnnouncer\\MessageAnnouncer.configuration.xml"'%item)
            os.system('copy MOTD.configuration.xml /Y "%s\\Rocket\\Plugins\\MOTD\MOTD.configuration.xml"'%item)
            os.system('copy MessageAnnouncer.dll /Y "%s\\Rocket\\Plugins\\MessageAnnouncer.dll"'%item)
            os.system('copy MOTD.dll /Y "%s\\Rocket\\Plugins\\MOTD.dll"'%item)
            os.system('copy RocketMod_TPA.dll /Y "%s\\Rocket\\Plugins\\RocketMod_TPA.dll"'%item)
            os.system('copy Permissions.config.xml /Y "%s\\Rocket\\Permissions.config.xml" '%item)
            os.system('copy Kits.configuration.xml /Y "%s\\Rocket\\Plugins\\Kits\\Kits.configuration.xml"'%item)
        else:
            print("%s ignored")%(item)

