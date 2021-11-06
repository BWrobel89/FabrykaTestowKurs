try:
    wait = WebDriverWait(driver,5)
    wait.until(ec.visibility_of_element_located(By.id, 'test'))
    print('iframe found')

except:
    print('there is no iframe')