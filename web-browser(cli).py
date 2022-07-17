try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = input("Search Here : ")
logo = '''
     _ _  _ _  _    _  _  ___  _  _  __  _  _  _  ___ 
    | U || | || |  | |// | __|| \| |/ _|| || \| || __|
    |   || U || |_ |  (  | _| | \\   ( |_n| || \\ || _| 
    |_n_||___||___||_|\\  |___||_|\_|\__/|_||_|\_||___|
             
             © Sumalya Chatterjee
   
   '''
print(logo )
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
    