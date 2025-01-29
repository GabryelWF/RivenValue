from selenium import webdriver
from selenium.webdriver.common.by import By
import time

weaponName = [
    'magistar', 'torid', 'verglas', 'ocucor', 'dual_toxocyst', 'ceramic_dagger', 'burston', 'bo', 'glaive',
    'okina', 'latron'
]

def equation(value):
    calcule = (value - 5) * 0.4
    approximation = round(calcule/10) * 10
    return approximation

def profit(sell, buy):
    profit = round((sell - buy) * 100 / sell, 1)
    return profit
    

def searchRiven(weaponName):
    
    driver = webdriver.Chrome()

    for weapon in weaponName:
        url = f"https://warframe.market/auctions/search?type=riven&weapon_url_name={weapon}&sort_by=price_asc"
        
        driver.get(url)
        time.sleep(2)  

        try:
            prices = driver.find_elements(By.CLASS_NAME, 'auction-entry__buyout')

            if prices:
                    textPrice = prices[0].find_element(By.CLASS_NAME, 'price--LQgqJ').text
                    buyPrice = equation(float(textPrice))
                    print(f"{weapon.capitalize()}: {textPrice}, Valor de Compra: {int(buyPrice)}, Lucro: {profit(float(textPrice), buyPrice)}%")
                    
            else:
                print(f"Preço não encontrado, arma {weapon}.")
        
        except Exception as e:
            print(f"Arma não encontrada, {weapon}: {e}")
    
    driver.quit()

searchRiven(weaponName)