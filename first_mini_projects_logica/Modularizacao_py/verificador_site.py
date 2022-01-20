import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except (urllib.error.URLError):
    print('Site indisponivel')
else:
    print('Site ok\n')
    print(f'Conteúdo html:')
    print(site.read())