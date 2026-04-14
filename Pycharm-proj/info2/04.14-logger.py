import logging
import re
from typing import List, Optional


class LogManager:
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    SUPPORTED_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    def __init__(self, log_file: str = 'application.log'):
        self.log_file = log_file
        self._logger = None
        self._setup_logging()

    def _setup_logging(self):
        self._handler = logging.FileHandler(self.log_file,
                                            encoding='utf-8')  # UTF-8 kódolás ajánlott a szabvány szerint
        self._formatter = logging.Formatter(self.LOG_FORMAT,
                                            self.DATE_FORMAT)  # JAVÍTÁS: Létre kell hozni a Formatter OBJEKTUMOT
        self._handler.setFormatter(
            self._formatter)  # HIBA VOLT: Itt a formatter OBJEKTUMOT kell átadni, nem a LOG_FORMAT stringet
        self._logger = logging.getLogger(type(self).__name__)  # Lekérjük a loggert az osztály neve alapján
        self._logger.setLevel(logging.DEBUG)  # Beállítjuk a minimum naplózási szintet
        if not self._logger.handlers:  # Ellenőrizzük, van-e már handler, hogy ne duplázzuk
            self._logger.addHandler(
                self._handler)  # HIBA VOLT: Ezt ki kell adni, különben a logger nem tudja, hova írjon

    def write_log(self, level: str, message: str):
        level = level.upper()  # Konvertálás nagybetűre a biztonság kedvéért
        if level not in self.SUPPORTED_LEVELS:  # Ellenőrzés a támogatott szintek listáján
            raise ValueError(f'Unsupported log level: {level}')  # Hiba, ha nem támogatott szintet kapunk

        numeric_level = getattr(logging, level, None)  # Megkeressük a szint számértékét a logging modulban
        if not isinstance(numeric_level, int):  # Ha nem számot kaptunk vissza, a szint érvénytelen
            raise ValueError(f'Invalid log level: {level}')  # Kivétel dobása

        self._logger.log(numeric_level, message)  # Tényleges írás a naplófájlba

    def read_logs(self, filter_levels: Optional[List[str]] = None) -> List[str]:
        filtered_lines = []  # Lista a talált soroknak
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:  # Fájl megnyitása olvasásra
                for line in f:  # Soronkénti beolvasás (memóriahatékonyabb, mint a readlines)
                    if filter_levels:  # Ha van megadva szűrő
                        if any(level.upper() in line for level in filter_levels):  # Ha a szint szerepel a sorban
                            filtered_lines.append(line.strip())  # Sor hozzáadása a listához, felesleges szóközök nélkül
                    else:
                        filtered_lines.append(line.strip())  # Ha nincs szűrő, minden mehet
        except FileNotFoundError:  # Ha a fájl még nem létezik
            return []  # Üres listával térünk vissza
        return filtered_lines  # Visszaadjuk a szűrt listát


if __name__ == "__main__":
    logger = LogManager()  # Példányosítás
    logger.write_log('INFO', 'Start app...')  # Teszt üzenet
    logger.write_log('ERROR', 'Task 1 error...')  # Teszt hiba
    logger.write_log('DEBUG', 'Task 1 error handling...')  # Teszt debug infó

    print("--- Szűrt naplóbejegyzések ---")  # Konzolos visszajelzés
    for log in logger.read_logs(['INFO', 'ERROR']):  # Csak az INFO és ERROR szintek kiírása
        print(log)  # Soronkénti megjelenítés