try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
print(r'''
  _  _ _   _ _    _  __  ___           _          
 | || | | | | |  | |/ / | __|_ _  __ _(_)_ _  ___ 
 | __ | |_| | |__| ' <  | _|| ' \/ _` | | ' \/ -_)
 |_||_|\___/|____|_|\_\ |___|_||_\__, |_|_||_\___|
    © Sumalya Chatterjee         |___/              
   ''')
try:
	# to search
	query = input("Search Here : ")
	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		print(j)
except KeyboardInterrupt:
	print("[-] Ctrl+C Detected")
