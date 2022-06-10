# Dell PowerEdge R710 Fan Controller API
 A Simple API made with Python Flask to help manage Dell PowerEdge R710 Enterprise Server's fan speeds remotely.
[![blog-post](https://raw.githubusercontent.com/ItsNee/Dell-PowerEdge-R710-Fan-Controller-API/main/img/SiteCover.jpg)](https://4pfsec.com/controlling-dell-poweredge-r710s-fans-remotely-with-an-api/)

[Checkout the full blog post here!](https://4pfsec.com/controlling-dell-poweredge-r710s-fans-remotely-with-an-api/)

## Installation
```bash
apt-get install git ipmitool python3 python3-pip -y
git clone https://github.com/ItsNee/Dell-PowerEdge-R710-Fan-Controller-API.git
cd Dell-PowerEdge-R710-Fan-Controller-API
pip install -r requirements.txt
```

## Server Usage
### Foreground
```bash
python3 api-server.py 
```
### Background
```bash
nohup python3 api-server.py&
```

## API Usage
| URL | Result |
| ------ | ------ |
| https://api.myserver.com/ | Returns a welcome string |
| https://api.myserver.com/get-temperature | Returns the server's temperature |
| https://api.myserver.com/set-fan-speed/<SPEED>/ | <SPEED> variable can be adjusted by end user |

![root](https://raw.githubusercontent.com/ItsNee/Dell-PowerEdge-R710-Fan-Controller-API/main/img/root.png)
![get-temp](https://raw.githubusercontent.com/ItsNee/Dell-PowerEdge-R710-Fan-Controller-API/main/img/get-temperature.png)
![set-fan-speed](https://raw.githubusercontent.com/ItsNee/Dell-PowerEdge-R710-Fan-Controller-API/main/img/set-fan-speed.png)

>-Nee
