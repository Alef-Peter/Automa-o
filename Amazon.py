from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

tabela = {'Produto': [],
          'Preço': []}


navegador = webdriver.Chrome()
navegador.get('https://www.amazon.com.br/s?bbn=16243890011&rh=n%3A16209062011%2Cn%3A%2116209063011%2Cn%3A16243803011%2Cn%3A16243890011%2Cp_89%3AApple&tag=hydrbrgk-20&ref=pd_sl_2f6lzeiv63_e')
time.sleep(2)


data_index = 0
try:
    raspagem = navegador.find_elements(By.XPATH, '//span[@data-component-type="s-search-results"]//span[@class="a-size-base-plus a-color-base a-text-normal"]')
    for i in raspagem:
        data_index += 1
        try:
            nome_produto = i.find_element(By.XPATH,
                                          f'//div[@data-index="{data_index}"]//*[@class="a-size-base-plus a-color-base a-text-normal"]').text
            preco_produto = i.find_element(By.XPATH,
                                           f'//div[@data-index="{data_index}"]//*[@class="a-price-whole"]').text
            tabela['Produto'].append(nome_produto)
            tabela['Preço'].append(preco_produto)
        except:
            data_index += 1
            print('Nenhum produto encontrado no elemento especificado ')
except:
    print ('Primeiro elemento não encontrado')


tabela_vendas = pd.DataFrame(tabela)
print(tabela_vendas)







