import requests
import json
import re
import cookie
import sys
import os
from tqdm import tqdm
from colorama import init, Fore, Style

PARENT_QUERY_HASH = "97b41c52301f77ce508f55e66d17620e"
COMMENTS_PER_PAGE = 50
BASE_OUTPUT_FOLDER = "output_comments"

def print_mipostify_ascii():
    init(autoreset=True)
    print(Fore.GREEN + r"""
███╗   ███╗██╗██████╗  ██████╗ ███████╗████████╗██╗███████╗██╗   ██╗
████╗ ████║██║██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██╔████╔██║██║██████╔╝██║   ██║███████╗   ██║   ██║█████╗   ╚████╔╝ 
██║╚██╔╝██║██║██╔═══╝ ██║   ██║╚════██║   ██║   ██║██╔══╝    ╚██╔╝  
██║ ╚═╝ ██║██║██║     ╚██████╔╝███████║   ██║   ██║██║        ██║   
╚═╝     ╚═╝╚═╝╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝        ╚═╝   
""" + Style.RESET_ALL)

def extract_shortcode_and_type(url):
    match = re.search(r"instagram\.com/(reel|p|tv)/([^/?#&]+)", url)
    if not match:
        return None, None
    content_type, shortcode = match.groups()
    return content_type, shortcode

def build_headers(shortcode, cookies_str):
    return {
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "Referer": f"https://www.instagram.com/p/{shortcode}/",  # aman untuk semua jenis
        "Cookie": cookies_str
    }

def graphql_request(query_hash, variables, headers):
    var_str = json.dumps(variables, separators=(",", ":"))
    url = (
        f"https://www.instagram.com/graphql/query/"
        f"?query_hash={query_hash}"
        f"&variables={requests.utils.quote(var_str)}"
    )
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"[!] HTTP {r.status_code} error for {query_hash}: {r.text}")
        return None
    return r.json()

def fetch_parent_comments(shortcode, headers):
    all_comments = []
    has_next = True
    cursor = ""
    page_count = 0

    progress_bar = tqdm(total=100, desc=f"Fetching {shortcode}", unit="page")

    while has_next:
        vars = {"shortcode": shortcode, "first": COMMENTS_PER_PAGE}
        if cursor:
            vars["after"] = cursor

        data = graphql_request(PARENT_QUERY_HASH, vars, headers)
        if not data:
            break

        try:
            edge_info = data["data"]["shortcode_media"]["edge_media_to_parent_comment"]
            edges = edge_info["edges"]
            for edge in edges:
                text = edge["node"]["text"]
                user = edge["node"]["owner"]["username"]
                all_comments.append(f"{user}: {text}")
        except KeyError as e:
            print(f"[!] Error parsing comment data: {e}")
            break

        page_info = edge_info["page_info"]
        has_next = page_info["has_next_page"]
        cursor = page_info["end_cursor"]

        page_count += 1
        progress_bar.n = page_count * COMMENTS_PER_PAGE
        progress_bar.last_print_n = progress_bar.n
        progress_bar.update(0)

    progress_bar.close()
    return all_comments

def main():
    print_mipostify_ascii()
    print("Masukkan beberapa URL Feed/Reel/TV (pisahkan dengan Enter, ketik 'done' untuk selesai):")
    urls = []
    while True:
        u = input("> ").strip()
        if u.lower() == "done":
            break
        urls.append(u)

    if not urls:
        print("[!] Tidak ada URL yang dimasukkan.")
        return

    # Siapkan folder output
    reels_folder = os.path.join(BASE_OUTPUT_FOLDER, "reels")
    feeds_folder = os.path.join(BASE_OUTPUT_FOLDER, "feeds")
    os.makedirs(reels_folder, exist_ok=True)
    os.makedirs(feeds_folder, exist_ok=True)

    # Ambil cookie dari modul
    sessionid = cookie.sessionid
    ds_user_id = cookie.ds_user_id
    csrftoken = cookie.csrftoken
    mid = cookie.mid
    cookies_str = f"sessionid={sessionid}; ds_user_id={ds_user_id}; csrftoken={csrftoken}; mid={mid};"

    for url in urls:
        content_type, shortcode = extract_shortcode_and_type(url)
        if not shortcode or not content_type:
            print(f"[!] URL tidak valid: {url}")
            continue

        headers = build_headers(shortcode, cookies_str)
        comments = fetch_parent_comments(shortcode, headers)

        if comments:
            if content_type == "reel":
                filename = os.path.join(reels_folder, f"comments_{shortcode}.txt")
            else:  # untuk 'p' atau 'tv'
                filename = os.path.join(feeds_folder, f"comments_{shortcode}.txt")

            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(comments))
            print(f"[+] {len(comments)} komentar disimpan ke {filename}")
        else:
            print(f"[!] Gagal mengambil komentar untuk {shortcode}")

if __name__ == "__main__":
    main()