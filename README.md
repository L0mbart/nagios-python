# nagios-python
add host, ip, alias di nagios

## edit nagios.cfg
```nano /usr/local/nagios/etc/nagios.cfg```

## tambahin line ini lalu save
```cfg_file=/usr/local/nagios/etc/objects/iboss.cfg```

## jalanin nagios.py

```python3 nagios.py```


## copy file nagios.cfg ke /usr/local/nagios/etc/objects/nagios.cfg

```reload service nagios```
```systemctl restart nagios```
