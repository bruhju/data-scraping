import re
import urllib.request
import bs4
from bs4 import BeautifulSoup

def textsaida(tam,id,cod,base):
    return('<li><input type="radio" class="tamanho__item_pdp js-tamanho__item_pdp" data-tamanho="'+tam+'" data-codigoproduto="'+cod+'" name="tamanho__id" id="tamanho__id'+tam+'" value="https://www.nike.com.br/Snkrs/Produto/'+base+'/153-169-211-'+id+'"><label for="tamanho__id'+tam+'">'+tam+'</label></li>')

def tamanhos(numero):
    tamanhos=['15,5','16','16,5','17','17,5','18','18,5','19','19,5','20','20,5','21','21,5','22','22,5','23','23,5','24','24,5','25','25,5','26','26,5','27','27,5','28','28,5','29','29,5','30','30,5','31','31,5','32','32,5','33','33,5','34','34,5','35','35,5','36','36,5','37','37,5','38','38,5','39','39,5','40','40,5','41','41,5','42','42,5','43','43,5','44','44,5','45','45,5','46','46,5','47','47,5','48','48,5','49','49,5','50','50,5','51']
    return tamanhos[numero]

# Entrada do link
link=str(input())


#Base Start
base= str(link)
base= re.sub('https://www.nike.com.br/Snkrs/Produto/','', base)
base= re.sub('/153-169-211-','', base)
base= re.sub('/1-16-210-','', base)
base= re.sub('/67-80-445-','', base)

#colocar outras duas GS e infantil
corte=base[-6:]
base= re.sub(corte,'', base)
#Base Finish

# Nome do Arquivo
nome=str("Cod-"+base+".txt")

# WebScaping Start
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html5lib')
list_item = soup.find('main', attrs={'class': 'container-fluid'})
name = list_item.text.strip()
text=str(name)
# WebScaping Finish

# Inicia o arquivo final
arquivo = open(nome, 'w')
arquivo.writelines('<ul class="variacoes-tamanhos__lista">')
arquivo.close()

i=0
while i<=70:#mudar limite
    k=tamanhos(i)
    if i%2==0:
        if re.search('"'+k+'":{"ProdutoId":"', text): # Float 
            aux = text.find('"'+k+'":{"ProdutoId":"')
            tam = k
            id = (text[aux+19:aux+29])
            cod=(text[aux+39:aux+53])
            s=textsaida(tam,id,cod,base)
            arquivo = open(nome, 'a')
            arquivo.writelines(s)
            arquivo.close()
    else:
        if re.search('"'+k+'":{"ProdutoId":"', text): # Integer
            aux1 = text.find('"'+k+'":{"ProdutoId":"')
            tam = k
            id = (text[aux1+19:aux1+25])
            cod=(text[aux1+37:aux1+49])
            s=textsaida(tam,id,cod,base)
            arquivo = open(nome, 'a')
            arquivo.writelines(s)
            arquivo.close()
    i=i+1  

arquivo = open(nome, 'a')
arquivo.writelines('</ul>')
arquivo.close()
# Finaliza o arquivo final