from selenium import webdriver
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get('/test')
async def test():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ["GOOGLE_CHROME_BIN"]
    driver = webdriver.Chrome(executable_path=os.environ["CHROMEDRIVER_PATH"], chrome_options=chrome_options)

    await driver.get("https://medium.com")
    print(driver.page_source)
    print("Finished!")
    return {'msg': 'success'}


if __name__ == '__main__':
    uvicorn.run('app:app', port=8080, debug=True, host='0.0.0.0')
