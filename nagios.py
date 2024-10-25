# script buat nambahin monitoring / device iboss ke file nagios.cfg biar cepet ga satu satu
# dibikin dulu daftar IP, hostname, dan alias yang mau ditambahin
hosts = [
    {"ip": "IP ADDRESS", "hostname": "HOSTNAME"},
    {"ip": "IP ADDRESS", "hostname": "HOSTNAME"},
    {"ip": "IP ADDRESS", "hostname": "HOSTNAME"},


# nama file konfigurasi dot cfg nya
config_file = "nagios.cfg"

# template untuk host dan service
host_template = """
define host {{
    use                     generic-host
    host_name               {hostname}
    alias                   {hostname}
    address                 {ip}
    check_command           check_ping!100.0,20%!500.0,60%
    max_check_attempts      5
    check_period            24x7
    notification_interval   30
    notification_period     24x7
}}
"""

service_template = """
define service {{
    use                     generic-service
    host_name               {hostname}
    service_description     PING
    check_command           check_ping!100.0,20%!500.0,60%
}}
"""

# nulis konfigurasi ke file
with open(config_file, "a") as f:
    for host in hosts:
        # Menambahkan host
        f.write(host_template.format(hostname=host["hostname"], ip=host["ip"]))
        # Menambahkan service
        f.write(service_template.format(hostname=host["hostname"]))

print(f"cihuyyyy konfigurasi iboss udah jadi, langsung reload aja service nagiosnya, filenya dibuat  ke  {config_file}")
