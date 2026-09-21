import re
import requests
from bs4 import BeautifulSoup


def print_secret_message(doc_url: str) -> None:
    html = requests.get(doc_url, timeout=30)
    html.raise_for_status()

    soup = BeautifulSoup(html.text, "html.parser")
    text = soup.get_text("\n")

    pattern = re.findall(r"(\d+)\s+(.)\s+(\d+)", text)
    points = [(int(x), ch, int(y)) for x, ch, y in pattern]

    if not points:
        print("No grid data found.")
        return

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, _, y in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, ch, y in points:
        grid[y][x] = ch

    for row in reversed(grid):
        print("".join(row))


print_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")



