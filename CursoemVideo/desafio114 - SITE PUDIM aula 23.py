import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.instagram.com')
except urllib.error.URLError:
    print('\033[31mO site não está acessível no momento.')
else:
    print('\033[32mConsegui acessar o site com sucesso!\033[m')
    print(site.read()) #conteúdo html do site que eu acabei de acessar.