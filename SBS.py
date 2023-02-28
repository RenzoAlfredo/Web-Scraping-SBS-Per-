## OBJETIVO: extraer todos los XLS de la web de la SBS
import bs4
import requests

# Url del que identificaremos los còdigos
url_base = 'https://www.sbs.gob.pe/app/stats_net/stats/EstadisticaBoletinEstadistico.aspx?p=2#'

# Url base desde el que haremos las descargas
url_base_desc = 'https://intranet2.sbs.gob.pe/estadistica/financiera/'


resultado_base = requests.get(url_base)

resultado_base_soup = bs4.BeautifulSoup(resultado_base.text, 'lxml')

#print(resultado_base_soup)

base_1 = resultado_base_soup.select(".nav-link")##[1]##["target"]
l = len(base_1)

print(base_1)

# lista de nombres de reportes
nombres_report_scrap = []
for i in range(0,l):
    nombres_report_scrap.append(base_1[i].getText())

print(nombres_report_scrap)

# lista de codigos para urls descarga
codigos_report_scrap = []
for j in range(0,l):
    codigos_report_scrap.append(base_1[j]["href"])

# eliminamos elementos duplicados
for d in codigos_report_scrap:
  while(codigos_report_scrap.count(d) > 1):
    codigos_report_scrap.remove(d)

# eliminamos elemento que no nos servirà
codigos_report_scrap.remove("javascript:void(0)")


codigos_report_scrap_final = []
for m in codigos_report_scrap:
    codigos_report_scrap_final.append(m.replace("EstadisticaSistemaFinancieroResultados.aspx?c=",""))

print(codigos_report_scrap)
print(codigos_report_scrap_final)

year = '2022'
month_c = 'se'
month_l = 'Setiembre'

for x in codigos_report_scrap_final:
    descarga = requests.get(url_base_desc + year + '/' + month_l + '/' + x + '-' + month_c + year + '.XLS')
    f = open(x + '-' + month_c + year + '.XLS', 'wb')
    f.write(descarga.content)
    f.close()











'''
mi_path = "nombres_report_scrap.txt"
f = open(mi_path, 'w')
for i in nombres_report_scrap:
    f.write(i)

f.close()
'''


