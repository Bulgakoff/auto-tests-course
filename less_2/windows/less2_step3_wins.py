from selenium import webdriver

browser = webdriver.Chrome()
curr_win_lst = browser.window_handles
current_win = browser.window_handles[0]
print(current_win)