from flask import Flask, jsonify
import pandas as pd
import matplotlib_inline as plt
import time
from selenium import webdriver


app = Flask(__name__)

@app.route('/') 

def index():

    options = webdriver.ChromeOptions()
    prefs ={"download.default_directory":"Users/juliocarvalho/Desktop/PosMapa/Bolsab3"}

    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options)
    driver.get ("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")

    btn_download = driver.find_element("link text",'Download')
    btn_download.click()

    time.sleep(3)

    driver.close()

    df = pd.read_csv("/Users/juliocarvalho/Desktop/Repositorio/Bolsab3/IBOVDia_10-11-22.csv",error_bad_lines=False, sep=';', skiprows=1)
    df.head()
    df.info()
    df.index[:-2]
    return "df.index"
if __name__ == "__main__":
    app.run()