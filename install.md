# Readme

## Installation instructions: 

### Soft-off-digital:

Before run the soft-off-digital files in our raspberry pi we need some libraries. 

- python3
- pip3
- pyserial

python 3 is already installed in our distro. So we have to install it 

```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install pyserial
```

This time we have two different files one is written in bash and another is written in Python 3, called soft-off-digital.sh and soft-off-digital.py respectly. 

### Serial port

then we have to activate the Serial port **/dev/ttyS0** 

```bash
sudo raspi-config
```

Go to 

- interfacing options
  - Serial

it asks if we want to use the Serial port to control the terminal we select 

**NO**

and if we want the serial port hardware enabled we select 

**YES** 

the terminal will show

```
The serial login shel is disabled 
The serial interfaces is enabled
```

Go to finish and reboot the raspberry pi. 

### moving files

Soft off digital.sh is installed in **/etc/init.d/**  to be opened in boot and execute the soft-off-digital.py installed in **/usr/local/bin/**

To do this we have to change some permissions and move them to the right path

```bash
sudo mv soft-off-digital.py /usr/local/bin/
sudo chmod +x /usr/local/bin/soft-off-digital.py
```

and: 

```
sudo mv soft-off-digital.sh /etc/init.d/
sudo chmod +x /etc/init.d/soft-off-digital.sh
sudo update-rc.d soft-off-digital.sh defaults
```

so now we can start or stop the daemon just typing in our terminal:

```
sudo /etc/init.d/soft-off-digital.sh start
```

and kill the daemon with 

```
sudo /etc/init.d/soft-off-digital.sh stop
```

