import requests
from bs4 import BeautifulSoup
import json 

def trade_geladeira(max_pages):
        page = 1
        while page <= max_pages:
                url = 'https://www.magazineluiza.com.br/geladeira-refrigerador/eletrodomesticos/s/ed/refr/' + str(page) + '/'
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "html.parser")
                for link in soup.findAll('a',class_= 'product-li'):
                        href = link.get("data-product")
                        data = json.loads(href)
                        sku = data['product']
                        titulo = data['title']
                        marca = data['brand']
                        modelo = data['reference']
                        preco = data['price']
                        cat = data['category']
                        sub = data['subCategory']
                        print('SKU: ' + sku)
                        print('TÍTULO:' + titulo)
                        print('MARCA: ' + marca)
                        print('MODELO: ' + modelo)
                        print('PREÇO = R$: ' + preco)
                        print('CATEGORIA: ' + cat)
                        print('SUBCATEGORIA: ' + sub)
                        print('-------------')
                page += 1
                return(sku,titulo,preco,cat,sub,modelo)

def trade_lavadora(max_pages):
        page = 1
        while page <= max_pages:
                url = 'https://www.magazineluiza.com.br/lavadora-de-roupas-lava-e-seca/eletrodomesticos/s/ed/ela1/' + str(page) + '/'
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "html.parser")
                for link in soup.findAll('a',class_= 'product-li'):
                        href = link.get("data-product")
                        href2 = link.get('title')
                        cat = href2.split(' ')
                        data = json.loads(href)
                        print('SKU: ' + data['product'])
                        print('TÍTULO:' + data['title'])
                        print('MARCA: ' + data['brand'])
                        print('MODELO: ' + data['reference'])
                        print('PREÇO = R$: ' + data['price'])
                        print('CATEGORIA: ' + data['category'])
                        print('SUBCATEGORIA: '+ data['subCategory']) 
                        print('-------------')
                page += 1 

trade_geladeira(1)
trade_lavadora(1)
