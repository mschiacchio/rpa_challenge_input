from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook

driver = webdriver.Chrome()
driver.get('https://www.rpachallenge.com/')

planilha = load_workbook('C:\\Users\\fiska\\OneDrive\\Área de Trabalho\\Marcelo_Teste\\challenge.xlsx')
folha = planilha['Sheet1']

#Campo First Name
valor_celula_fname = folha['A2'].value
campo_first_name = driver.find_element(By.CLASS_NAME, 'labelFirstName')
campo_first_name.send_keys(valor_celula_fname)

#Campo Last Name
valor_celula_lname = folha['B2'].value
campo_last_name = driver.find_element(By.CLASS_NAME, 'labelLastName')
campo_last_name.send_keys(valor_celula_lname)

#Campo Company Name
valor_celula_cname = folha['C2'].value
campo_company_name = driver.find_element(By.CLASS_NAME, 'labelCompanyName')
campo_company_name.send_keys(valor_celula_cname)

#Campo Role in Company
valor_celula_rcompany = folha['D2'].value
campo_role_in_company = driver.find_element(By.CLASS_NAME, 'labelRole')
campo_role_in_company.send_keys(valor_celula_rcompany)

#Campo Address
valor_celula_address = folha['E2'].value
campo_address = driver.find_element(By.CLASS_NAME, 'labelAddress')
campo_address.send_keys(valor_celula_address)

#Campo email
valor_celula_email = folha['F2'].value
campo_email = driver.find_element(By.CLASS_NAME, 'labelEmail')
campo_email.send_keys(valor_celula_email)

#Campo Phone Number
valor_celula_phone = folha['G2'].value
campo_phone_number = driver.find_element(By.CLASS_NAME, 'labelPhone')
campo_phone_number.send_keys(valor_celula_phone)

botao_submit = driver.find_element(By.ID, 'btn uiColorButton')
botao_submit.click()







