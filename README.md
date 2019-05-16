# ColetaQoE
Para obter dados de video

# Requisitos

## AP

```
sudo apt-get install -y hostapd iw tcpdump wireless-tools
```

## Estação


```
sudo apt-get install -y wpasupplicant firefox git nodejs npm
git clone https://github.com/h3dema/server.js
cd server.js/server
npm install fs os express
```


# Configuração do AP

* hostapd.conf: configuração do hostapd para coleta
* hostapd.access: lista dos MACs da interface wifi das estações, para permitir conexão sem senha

## Ativando o AP

1) Para colocar o hostapd rodando
```bash
cd ColetaQoE
sudo hostapd hostapd.conf  &
```

2) Para ter acesso TCP
```bash
sudo ifconfig wlan0 192.168.0.1
sudo iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j MASQUERADE
sudo echo "1" >/proc/sys/net/ipv4/ip_forward
```

# Configuração das estações

* wpa_supplicant.conf: arquivo com a configuração do wpa-supplicant para conectar no AP

## Ativando Estação

1) Conectar no AP

```bash
cd ColetaQoE
sudo wpa_supplicant -i wlan0 -c wpa_supplicant.conf  &
```

2) Para ter acesso TCP

```bash
sudo ifconfig wlan0 192.168.0.x
sudo route del -net 150.164.10.0/25
sudo route del -net 0/0 gw 150.164.10.1
sudo route del -net 0/0 gw 192.168.0.1
```
Substituir __x__ pelo endereço do cliente {2, 3, ....}.


# Dicas de instalação

## Erro de acesso
Se você encontrar um erro do tipo __"Error: CERT_UNTRUSTED"__, você precisará executar um ou ambos os comandos listados abaixo:

```
npm config set strict-ssl false
npm config set registry="http://registry.npmjs.org/"
```
## Biblioteca faltando

Se você encontrar o erro __"Error: Cannot find module 'body-parser'"__ ao tentar executar o servidor node.js, você precisará instalar um modulo adicional:

```
npm install body-parser
```
