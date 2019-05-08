# Configurando o roteamento nas estações

## acrescentar uma rota para acesso via rede local

winet@fenrir:~$ sudo route add -net 150.164.10.0/25 dev eth0
winet@fenrir:~$ route -n
Tabela de Roteamento IP do Kernel
Destino         Roteador        MáscaraGen.    Opções Métrica Ref   Uso Iface
0.0.0.0         150.164.10.1    0.0.0.0         UG    0      0        0 eth0 <<< retirar esta agora (2)
150.164.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
150.164.10.0    0.0.0.0         255.255.255.128 U     0      0        0 eth0 <<< acrescentei esta (1)
150.164.10.0    0.0.0.0         255.255.255.128 U     0      0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.0.0     0.0.0.0         255.255.255.0   U     0      0        0 wlan0

## retirar a rota default via eth0

winet@fenrir:~$ sudo route del -net 0/0 gw 150.164.10.1
winet@fenrir:~$ route -n
Tabela de Roteamento IP do Kernel
Destino         Roteador        MáscaraGen.    Opções Métrica Ref   Uso Iface
150.164.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
150.164.10.0    0.0.0.0         255.255.255.128 U     0      0        0 eth0
150.164.10.0    0.0.0.0         255.255.255.128 U     0      0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.0.0     0.0.0.0         255.255.255.0   U     0      0        0 wlan0

## considerando que o AP tem o endereço 192.168.0.1

winet@fenrir:~$ sudo route add -net 0/0 gw 192.168.0.1
winet@fenrir:~$ route -n
Tabela de Roteamento IP do Kernel
Destino         Roteador        MáscaraGen.    Opções Métrica Ref   Uso Iface
0.0.0.0         192.168.0.1     0.0.0.0         UG    0      0        0 wlan0 << acrescentei esta agora (3)
150.164.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
150.164.10.0    0.0.0.0         255.255.255.128 U     0      0        0 eth0
150.164.10.0    0.0.0.0         255.255.255.128 U     0      0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.0.0     0.0.0.0         255.255.255.0   U     0      0        0 wlan0



# Diagrama de rede

                   +------------+                           +------------+
                   |      AP    |                           |     STA    |
     150.164.10.yy |            |           wifi            |            |
      internet ----|eth0  wlan0 |---------------------------|wlan0   eth0|---- rede de controle
          |        |192.168.0.1    192.168.0.x |            |            |150.164.10.yy
          |        +------------+                           +------------+
          |
          |
          | dash.winet.dcc.ufmg.br
          | 150.164.10.51
   +------------+
   |  servidor  |
   |  de video  |
   +------------+
