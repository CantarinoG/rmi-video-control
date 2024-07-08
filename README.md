
# Como rodar:

* Name Server: Iniciar o nameserver com ``` python3 -m Pyro4.naming -n <ip da maquina que vai rodar o nameserver> ```
* Para pegar seu ip, utilize o seguinte comando no terminal: ``` ifconfig ``` caso seja Linux ou ``` ipconfig ``` caso seja windows.
  Ex: proucure por algo como ```192.168.3.8```
* Trocar a variavel ip no data.py pelo seu ip obtido.
* Servidores dos vídeos: Iniciar o video_server.py passando o index do vídeo que será reproduzido. Ex ``` python3 video_server.py 0 ```
* Cliente: Rodar client.py (```python3 cmi_client.py```),
* Client com Interface Gráfica: Rodar o client.py(```flet run client.py```)

### O que precisa instalar para funcionar:
    pip install Pyro4 opencv-python 

### O que precisa instalar para visualizar a interface gráfica:
    pip install flet


