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


# Configuração das estações

* wpa_supplicant.conf: arquivo com a configuração do wpa-supplicant para conectar no AP


# Dicas de instalação

Se você encontrar um erro do tipo __"Error: CERT_UNTRUSTED"__, você precisará executar um ou ambos os comandos listados abaixo:

```
npm config set strict-ssl false
npm config set registry="http://registry.npmjs.org/"
```
