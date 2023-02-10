import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import pyperclip

def Read_Customer_File(Choices):
    global Customers_lists
    TEXT_FILE1 = 'Txt_files/Customer.txt'
    TEXT_FILE2 = 'Txt_files/Customer2.txt'
    Customers_lists = []
    if Choices == 1:
        text_file = open(TEXT_FILE1,encoding='utf-8')
    else:
        text_file = open(TEXT_FILE2,encoding='utf-8')
    Customers_lists = text_file.readlines()
    for name in Customers_lists:
        Name = name.replace('\n','')
        Customers_lists[Customers_lists.index(name)] = Name

def Read_Finished_File():
    global Finished_lists
    TEXT_FILE = 'Txt_files/Finish.txt'
    Finished_lists = []
    text_file = open(TEXT_FILE,encoding='utf-8')
    Finished_lists = text_file.readlines()
    for name in Finished_lists:
        Name = name.replace('\n','')
        Finished_lists[Finished_lists.index(name)] = Name

def Read_Problem_File(Choices):
    global Problem_lists
    TEXT_FILE1 = 'Txt_files/ProblemList.txt'
    TEXT_FILE2 = 'Txt_files/ProblemList2.txt'
    Problem_lists = []
    if Choices == 1:
        text_file = open(TEXT_FILE1,encoding='utf-8')
    else:
        text_file = open(TEXT_FILE2,encoding='utf-8')
    Problem_lists = text_file.readlines()
    for name in Problem_lists:
        Name = name.replace('\n','')
        Problem_lists[Problem_lists.index(name)] = Name

def Read_Blocked_File(Choices):
    global Blocked_lists
    TEXT_FILE1 = 'Txt_files/Blocked.txt'
    TEXT_FILE2 = 'Txt_files/Blocked2.txt'
    Blocked_lists = []
    if Choices == 1:
        text_file = open(TEXT_FILE1,encoding='utf-8')
    else:
        text_file = open(TEXT_FILE2,encoding='utf-8')
    Blocked_lists = text_file.readlines()
    for name in Blocked_lists:
        Name = name.replace('\n','')
        Blocked_lists[Blocked_lists.index(name)] = Name
   
def Read_Fail_File():
    global Fail_lists
    TEXT_FILE1 = 'Txt_files/Failed.txt'
    Fail_lists = []
    text_file = open(TEXT_FILE1,encoding='utf-8')
    Fail_lists = text_file.readlines()
    for name in Fail_lists:
        Name = name.replace('\n','')
        Fail_lists[Fail_lists.index(name)] = Name

def Write_Finished_File(name):
    TEXT_FILE2 = 'Txt_files/Finish.txt'
    finished_file = open(TEXT_FILE2,"a",encoding='utf-8')
    finished_file.write(name)
    finished_file.write('\n')

def Write_Blocked_File(name,Choices):
    TEXT_FILE1 = 'Txt_files/Blocked.txt'
    TEXT_FILE2 = 'Txt_files/Blocked2.txt'
    if Choices == 1:
        Blocked_file = open(TEXT_FILE1,"a",encoding='utf-8')
    else:
        Blocked_file = open(TEXT_FILE2,"a",encoding='utf-8')
    Blocked_file.write(name)
    Blocked_file.write('\n')

def Write_Problem_File(name,Choices):
    TEXT_FILE1 = 'Txt_files/ProblemList.txt'
    TEXT_FILE2 = 'Txt_files/ProblemList2.txt'
    if Choices == 1:
        ProblemList_file = open(TEXT_FILE1,"a",encoding='utf-8')
    else:
        ProblemList_file = open(TEXT_FILE2,"a",encoding='utf-8')
    ProblemList_file.write(name)
    ProblemList_file.write('\n')

def Write_Failed_File(name):
    TEXT_FILE1 = 'Txt_files/Failed.txt'
    Failed_file = open(TEXT_FILE1,"a",encoding='utf-8')
    Failed_file.write(name)
    Failed_file.write('\n')

def AddBrackets(url):
    increase = 0

    for Index in range(0,len(url)-1):
        Index += increase
        char = url[Index]
        bIsNotNumeric = not(char.isnumeric())
        bIsNotAlphabet = not(char.isalpha())
        bIsNotBracket = char != '{' and char != '}'
        bDoesNotHaveBracket = (url[Index-1] != '{')
        if bIsNotNumeric and bIsNotAlphabet  and bIsNotBracket and bDoesNotHaveBracket:
            url = url[:Index] + '{' + char + '}' + url[Index+1:]
            increase +=2

    return url

# Constants
PATH = "C:/Users/User/Desktop/chromedriver_win32/chromedriver.exe"
GMAIL = 'yourGmail'
PASSWORD = 'password'
PAGE = ['Boomer','小芸-保健之家']

# For slow Method
SAVED_REPLIES_LIST = ['8/1']
SAVED_PICTURE_LIST = []
MAX_REPLY = 5

# For Fast Method
TEXT_LIST = ["testing","1","2"]
VIDEO_PATH_LIST = [r"C:\Users\User\Desktop\workspace\python\webcrawler\Rick.mp4",r"C:\Users\User\Desktop\workspace\python\webcrawler\Rick.mp4"]
PICTURE_PATH_LIST = [r"C:\Users\User\Desktop\workspace\python\webcrawler\rickroll_4k.jpg",r"C:\Users\User\Desktop\workspace\python\webcrawler\rickroll_4k.jpg"]



class Facebook_Bot:
    def __init__(self):
        self.url = "https://www.facebook.com/messages/t/100008694106310"
        self.Choice = 1

    def AskForMethod(self):
        while True:
            self.Method = input("1: Fast, no input allow, 2: slow input allow:")
            if self.Method == '1' or self.Method == '2':
                break
            else:
                print("!Please Input 1 or 2!")
            
    # Simple Functions
    def OpenFacebook(self):
        # Open facebook
        # Creating Instance
        option = Options()

        # Working with the 'add_argument' Method to modify Driver Default Notification
        option.add_argument('--disable-notifications')

        # Passing Driver path alongside with Driver modified Options
        self.driver = webdriver.Chrome(executable_path= PATH, chrome_options= option)
        self.driver.get(self.url)

    def Login(self):
        # Login
        login_email = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.NAME, 'email')))
        login_password = self.driver.find_element_by_name('pass')
        login_email.send_keys(GMAIL)
        login_password.send_keys(PASSWORD)
        login_password.send_keys(Keys.RETURN)


    def ClickInboxButton(self):
        try:
            inbox_button = WebDriverWait(self.driver, 30).until( 
                EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/label/input'))
            )
            inbox_button.click()
            time.sleep(2)
        except TimeoutException:
            print("####Error:The 'inbox_button' can't be clicked, trying again...")
            self.ClickInboxButton()
    
    def ReadAllFiles(self):
        Read_Customer_File(self.Choice)
        Read_Finished_File()
        Read_Problem_File(self.Choice)
        Read_Blocked_File(self.Choice)
        Read_Fail_File()

    def Is_Finished(self,name): # True:finished, False:not finished
        Read_Finished_File()
        if name in Finished_lists:
            return True
        else:
            return False

    def Is_Blocked(self,name): # True:Blocked, False:not Blocked
        time.sleep(1)
        try:
            detectBlockElement = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]'))
            )
            return False
        except TimeoutException:
            # Cant send message to the user, blocked
            # Add the name to blocked file
            print(f"####Error:{name} has blocked you, if he didn't, check 'detectBlockElement' which has same path as 'message_box'")
            Write_Blocked_File(name,self.Choice)
            return True   

    def In_BlockedFile(self,name): # True:Blocked, False:not Blocked
        Read_Blocked_File(self.Choice)
        if name in Blocked_lists:
            return True
        else:
            return False
    
    def Has_Problem(self,name): # True: Has problem, False: no problem
        Read_Problem_File(self.Choice)
        if name in Problem_lists:
            return True
        else:
            return False

    def Failed(self,name):
        Read_Fail_File()
        if name in Fail_lists:
            return True
        else:
            return False

    def GetCustomersName(self):
        for Name in Customers_lists:
            if self.In_BlockedFile(Name) or self.Is_Finished(Name) or self.Failed(Name):
                pass
            else:
                return Name
    
    def ClearName(self):
        SearchBar = WebDriverWait(self.driver, 30).until(   
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/label/input'))
            )
        SearchBar.clear()
        # try:
        #     ClearButton = WebDriverWait(self.driver, 30).until( 
        #         EC.presence_of_element_located((By.XPATH, '//*[@id="facebook"]/body/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/a'))
        #     )                                              
        #     ClearButton.click()
        # except TimeoutException:
        #     print("####Error:The 'ClearButton' can't be found, trying again...")
        #     self.ClickInboxButton()
    
    def EnterName(self,name):
        time.sleep(0.5)
        # Find search bar
        try:
            SearchBar = WebDriverWait(self.driver, 30).until(   
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/label/input'))
            )
            SearchBar.send_keys(name)
            time.sleep(1)
            UserProfile = WebDriverWait(self.driver, 30).until( 
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span'))
            ) 
            UserProfile.click()
            
        except TimeoutException:
            print("####Error:The 'SearchBar' can't be found, trying again...")
            self.EnterName(name)

    def EnterName_OneByOne(self,name):
        try:
            time.sleep(1)
            SearchBar = WebDriverWait(self.driver, 30).until(   
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/label/input'))
            )
            for char in name:
                SearchBar.send_keys(char)
                if len(name) <= 2:
                    time.sleep(1.75)
                if len(name) <= 4:
                    time.sleep(1)
                else:
                    if name.index(char)+1 <= len(name)/2:
                        time.sleep(0.5)
            UserProfile = WebDriverWait(self.driver, 30).until( 
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span'))
            ) 
            UserProfile.click()
        except TimeoutException:
            print("####Error:The 'SearchBar' can't be found, trying again...")
            self.EnterName(name)

    def CanBeSearch(self,name): # True: User can be searched, False: User cannot be searched
        time.sleep(1)
        try:
            User = WebDriverWait(self.driver, 30).until( 
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/a/div[2]/div/div[1]/h1/span/span'))
            ) 
            if User.text == name:
                return True
            else:
                return False
                
        except TimeoutException:
            print(f"####Error:{name} can't be found, if this message appear twice and {name} exist, check 'User' and 'User2' class name")
            return False

    def SearchName(self,name): # True: User is Selected, False: User doesn't exist
        time.sleep(0.5)
        if self.Has_Problem(name):
            self.EnterName_OneByOne(name)
            bCanBeSearched = self.CanBeSearch(name)
            if bCanBeSearched == False:
                Write_Failed_File(name)
                return False
            else:
                return True
        else:
            self.EnterName(name)
            bCanBeSearched = self.CanBeSearch(name)
            if bCanBeSearched:
                return True
            elif bCanBeSearched == False and self.Has_Problem(name):
                Write_Failed_File(name)
                return False
            else:
                Write_Problem_File(name,self.Choice)
                self.ClearName()
                self.SearchName(name)

    # Method 1
    def METHOD1(self):
        # Send Video
        for VideoPaths in VIDEO_PATH_LIST:
            self.InsertFile(VideoPaths)

        # Send Picture by path
        for PicPaths in PICTURE_PATH_LIST:
            self.InsertFile(PicPaths)
            
        # Send Text
        for Text in TEXT_LIST:
            self.SendMessage(Text)

    # Functions for method 1
    def InsertFile(self,Path):
        while True:
            try:
                FileEmbedIcon = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/span/div'))
                )
                FileEmbedIcon.click()
            except TimeoutException:
                print("####Error:'FileEmbedIcon' can't be found, check its path")
                self.InsertFile(Path)
            time.sleep(1)
            while True:
                a = autoit.control_focus("Open", "Edit1")
                if (a == 1):
                    break
            autoit.control_set_text("Open", "Edit1", Path)
            path = autoit.control_get_text("Open", "Edit1")
            if path == Path:
                break
        autoit.control_send("Open","Edit1","{ENTER}")
        self.CheckIfFileInserted(Path)
    
    def CheckIfFileInserted(self,Path):
        try:
            iconAfterFileEmbed = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div[1]/i')))
            time.sleep(1)
            message_box = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div[2]/div/div[1]'))) 
            message_box.send_keys(Keys.RETURN)
        except TimeoutException:
            print("####Error:'iconAfterFileEmbed' can't be found, check its path, trying...")
            self.CheckIfFileInserted(Path)

    def SendMessage(self,Text):
        try:
            time.sleep(0.2)
            while True:
                message_box = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')))
                pyperclip.copy(Text)
                message_box.send_keys(Keys.CONTROL+ "v")
                time.sleep(0.2)
                if message_box.text != " ":
                    break
            message_box.send_keys(Keys.RETURN)
            time.sleep(0.2)
        except TimeoutException:
            print("####Error:'message_box' can't be found, check its path, trying...")
            self.SendMessage(Text)

# Main    
Bot = Facebook_Bot()
Bot.OpenFacebook()
Bot.Login()
Bot.ClickInboxButton()
Bot.ReadAllFiles()
runtime = 0
while True:
    Name = Bot.GetCustomersName()
    CanBeSearched = Bot.SearchName(Name)
    IsBlocked = Bot.Is_Blocked(Name)
    if CanBeSearched and IsBlocked==False:# User can be searched and doesn't block you
        Bot.METHOD1()
        # Add name to finished file
        Write_Finished_File(Name)  
    else:
        print(Name)
    Bot.ClearName()
    runtime += 1