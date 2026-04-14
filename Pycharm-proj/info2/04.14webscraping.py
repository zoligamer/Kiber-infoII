import requests
import requests_cache
from bs4 import BeautifulSoup
import textwrap  # ÚJ: Beépített modul a szöveg tördeléséhez


def scraping_os():
    os_list = {}  # Szótár az operációs rendszereknek
    description_text = ""  # Változó a bevezető szövegnek
    kernel_list = []  # Lista a kernel típusoknak
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.166 Safari/537.36',
    }

    session = requests_cache.CachedSession("wiki_os_hu")
    session.headers.update(headers)
    response = session.get(
        "https://hu.wikipedia.org/wiki/Oper%C3%A1ci%C3%B3s_rendszer",
    )

    print(f"From cache: {hasattr(response, 'from_cache')}")
    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all(attrs={'aria-labelledby': 'Operációs_rendszer_változatok'})
    description_elements = soup.find_all(attrs={'data-mw-section-id': '0'})
    kernel_section = soup.find(attrs={'data-mw-section-id': '2'})

    for section in sections:
        all_link = section.find_all("a")
        for link in all_link:
            if link.parent.name == "li":
                os_name = link.get_text(strip=True)
                os_link = link.get('href')
                os_list[os_name] = os_link

    for section in description_elements:
        paragraphs = section.find_all("p")
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                # JAVÍTÁS: Itt tördeljük a bekezdést 80 karakter szélességre
                wrapped_p = textwrap.fill(text, width=80)  # Automatikus tördelés beállítása
                description_text += wrapped_p + "\n\n"  # Tördelt szöveg és dupla sorköz hozzáadása

    if kernel_section:
        for li in kernel_section.find_all("li"):
            kernel_list.append(li.get_text(strip=True))

    return os_list, description_text, kernel_list


if __name__ == "__main__":
    os_dict, full_desc, kernels = scraping_os()

    print("find os wiki")
    for name in os_dict:
        print(f"\t-{name},({os_dict[name]})")

    print("\n--- Description ---")
    print(full_desc)  # Itt már a tördelt szöveg fog megjelenni

    print("\n--- Kernel Types (Section 2) ---")
    for k in kernels:
        print(f"\t-{k}")