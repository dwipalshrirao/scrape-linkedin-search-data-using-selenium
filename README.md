# scrape-linkedin-search-data-using-selenium
  
  This python script Scrapes "data analyst job" search data from "linkedin" using Python's library selenium.
  
  ## Features:
  This script is able to scrape job position, company name, and company location from linkedin. Normally, if we try to scrape data from linkedin, it will give 20 to 25 companies because of lazy load feature. This script automatically scroll down screen upto the end of page and then scrape data.
  
  ## Technology used:
  
  * python
  * selenium
  * Numpy
  * Pandas
  
  I have used Numpy , Pandas for processing data. You can use your logic and can skip these libraries.
  
   ### Run the following commands to get started your project:
    
   1. download project

  ```
  git clone https://github.com/dwipalshrirao/scrape-linkedin-search-data-using-selenium

  cd scrape-linkedin-search-data-using-selenium

  ```
  
  2. webdriver setup
  
  you need to setup webdriver according to which browser you are using. visite [this link](https://pypi.org/project/webdriver-manager/) and select code according to your browser. It will download webdriver automatically.
  
    ![webdriver](https://github.com/dwipalshrirao/scrape-linkedin-search-data-using-selenium/blob/main/webdriver.png)
 
 
  
  3. run command below

  ```
  python linkedin.py
  
  ```


