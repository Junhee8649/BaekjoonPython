n, m = map(int, input().split())
site_pwd = {}

for i in range(n):
    site, pwd = input().split()
    site_pwd[site] = pwd

for j in range(m):
    search_site = input()
    print(site_pwd[search_site])