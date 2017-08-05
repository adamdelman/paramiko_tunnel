# paramiko_tunnel

Native Python SSH tunnel based on Paramiko.  
Inspired by code from: https://github.com/paramiko/paramiko/blob/master/demos/forward.py


Example usage
-------------
~~~
import paramiko
import paramiko_tunnel
import requests

client = paramiko.SSHClient()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy(),
)
client.connect(
    hostname='192.168.0.1',
    port=22,
    username='user',
    password='hunter2',
)
tunnel = paramiko_tunnel.tunnel.Tunnel(
    paramiko_session=client,
    dest_host='192.168.0.2',
    dest_port=80,
)

response = requests.get(
    url='http://{bind_addr}:{bind_port}'.format(
        bind_addr=tunnel.bind_address,
        bind_port=tunnel.bind_port,
    )
).content
print(response)
~~~