from user_agent import generate_user_agent


head = {
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
}

uklon1 = {
    "client_id": "6289de851fc726f887af8d5d7a56c635",
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
}

uklon2 = {
    "client_id": "6289de851fc726f887af8d5d7a56c635",
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
}

frisor = {
    "Content-type": "application/json",
    "Accept": "application/json, text/plain",
    "authorization": "Bearer yusw3yeu6hrr4r9j3gw6",
    "User-Agent": generate_user_agent(),
    "cookie": "auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1",
}

zakaz = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Referer": "https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
    "User-Agent": generate_user_agent(),
    "x-chain": "megamarket",
}
