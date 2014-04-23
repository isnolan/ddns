ddns
====

ddns for dnspod


### how to use
+ seting python file
```sh
# replace your infomation
sudo vim dnspod.py 

# copy to bin folder
sudo mv dnspod.py /usr/bin/dnspod

# set permissions information
sudo chmod +x /usr/bin/dnspod
sudo chown root:wheel /usr/bin/dnspod
```

+ seting launch plist
```sh
# replace your infomation, you can replace yhostc from filename and file content
sudo vim com.yhostc.dnspod.plist

# copy to launch folder
sudo mv com.yhostc.dnspod.plist /Library/LaunchDaemons/

# set permissions information
sudo chown -R root:wheel /Library/LaunchDaemons/com.yhostc.dnspod.plist
sudo chmod 644 /Library/LaunchDaemons/com.yhostc.dnspod.plist
```

+ reboot your mac
