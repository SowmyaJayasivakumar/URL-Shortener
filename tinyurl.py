import pyshorteners

link = input("Enter a url : \n")
short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("Shortened url: ")
print(x)
