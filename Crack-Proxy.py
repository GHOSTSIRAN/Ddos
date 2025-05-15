import requests


proxy_apis = [
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://www.proxy-list.download/api/v1/get?type=all",
    "https://www.proxy-list.download/api/v1/get?type=elite",
    "https://www.proxy-list.download/api/v1/get?type=transparent",
    "https://www.proxy-list.download/api/v1/get?type=high_anonymous",
    "https://www.proxy-list.download/api/v1/get?type=low_anonymous",
    "https://www.proxy-list.download/api/v1/get?type=shared",
    "https://www.proxy-list.download/api/v1/get?type=anonymous",
    "https://www.proxy-list.download/api/v1/get?type=elite_socks5",
    "https://www.proxy-list.download/api/v1/get?type=all_socks5",
    "https://www.proxy-list.download/api/v1/get?type=elite_http",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://api.getproxylist.com/proxy?allowsHttps=true",
    "https://spys.me/proxy.txt",
    "https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc",
    "https://www.proxynova.com/proxy-server-list/",
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/",
    "https://www.us-proxy.org/",
    "https://www.socks-proxy.net/",
]


def fetch_proxies():
    proxies = set()  
    for url in proxy_apis:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  
            
            if response.headers['Content-Type'].strip().startswith('text'):
                proxies.update(response.text.splitlines())
        except Exception as e:
            print(f"Error fetching from {url}: {e}")
    
    return list(proxies)


def main():
    all_proxies = fetch_proxies()  

    
    with open('proxy-list.txt', 'w') as f:
        for proxy in all_proxies:
            f.write(f"{proxy}\n")

    print(f"تعداد پروکسی‌های جمع‌آوری شده: {len(all_proxies)}")

if __name__ == "__main__":
    main()