
# Practice on how to split strings based on delimiter
# s = "Aisha;Benny;Chloe;David;Eva"
# delimiter = ";"
# currentpos = 0 
# parts = [] 
# while True:
#     delim_start = s.find(";",currentpos)
#     if delim_start == -1: 
#         word = s[currentpos:]
#         parts.append(word)
#         break
#     word = s[currentpos:delim_start]

#     currentpos = delim_start + len(";")
#     parts.append(word)
    
# print(parts)
#################################################################
#################################################################

# Scenario 1: Spltting multiple sentences in an article
# You are developing a text-cleaning tool for an editorial website. 
# Your program must extract words based on commas 
# while keeping the sentence structure intact into a list.

# expected output
# ["The modern world has become highly interconnected",
#  "with technology playing a crucial role in every aspect of our lives"
#  ...]

s = "The modern world has become highly interconnected,with technology playing a crucial role in every aspect of our lives,from communication and healthcare to finance and education. People rely on digital tools for their daily tasks,making it essential to understand how to secure personal information and ensure data privacy. With the rise of social media,the sharing of information has become instantaneous,bringing both opportunities and challenges. Cybersecurity threats are on the rise,requiring individuals and organizations to take precautions against potential hacks,data breaches,and identity theft."


# write your code here
currentpos = 0
delimiter = "," 
whole_sentence = []
while True:
    delim_start = s.find(",",currentpos)
    if delim_start == -1:
        sentence = s[currentpos:]
        whole_sentence.append(sentence)
        break
    sentence = s[currentpos:delim_start]
    whole_sentence.append(sentence)
    currentpos =   delim_start + len(",")

print(whole_sentence)


######################################################

# Scenario 2: Extracting URLs from a Web Log
# You are a web analyst at a large company handling 
# log files from multiple servers. Your task is to extract URLs 
# from a comma-separated web traffic log into a list for further analysis.

# expected output
# ['https://shopnow.com', 'https://newsdaily.com', 'https://techinsider.org', ... ]
weblogs = "https://shopnow.com,https://newsdaily.com,https://techinsider.org,https://myblog.net,https://travelhub.io,https://educonnect.edu,https://cryptoexchange.com,https://gamingworld.gg,https://sportsupdates.tv,https://moviemagic.net,https://musicstream.fm,https://fitnessclub.org,https://foodiesdelight.com,https://financeguru.biz,https://shoppinghub.co,https://bookreviews.xyz,https://jobportal.jobs,https://weatherwatcher.gov,https://luxuryhomes.realestate,https://carenthusiast.auto"


# write your code here






#################################################################

# Scenario 3: Extracting Product IDs from a Manufacturing System Log

# You are working with a manufacturing system that records 
# product IDs in a single string. However, instead of using 
# a single-character delimiter, the system separates product 
# IDs using a multi-character delimiter (///).

# Your task is to:
# (1) Extract individual product IDs from the raw string and store them in a list.
# (2) Convert each extracted ID into an integer for further processing.
    
product_data = "1001///1023///1500///2034///3102///4025///5011///6098///7103///8020"

# write your code here





########################################################

# Scenario 4: Extracting Stock Prices for Market Analysis
# You are working for a stock exchange where hourly stock prices 
# for nVidia are recorded in a colon-separated string. 
# Your task is to extract all hourly stock prices 
# into a list of floats for further calculations.

# expected output
# [154.2, 158.7, 160.1, 163.4]

stockprice = "154.2:158.7:162.9:160.1:163.4:165.8:159.5:161.2:167.3:162.0:169.4:172.5:171.8:168.2:166.0:175.4:177.9:180.2:178.6:182.1:185.3:190.5:188.2:191.0:193.5:195.8:199.1:200.7:202.3:198.9"

# write your code here


#######################################################

# Scenario 5: Extracting IP Addresses from a Server Log
# A cybersecurity specialist needs to analyze suspicious 
# activity in a company’s network. The firewall logs contain 
# IP addresses separated by commas. 
# Your task is to extract all unique IP addresses into a list
# for further investigation.

# expected output
# ["192.168.1.1", "10.0.0.2", "172.16.5.10"]

ipadds = "192.168.1.1,10.0.0.2,172.16.5.10,192.168.1.45,10.0.0.18,172.16.5.20,192.168.2.15,10.0.0.5,172.16.5.30,192.168.3.5,10.0.0.12,172.16.6.25,192.168.1.100,10.0.0.9,172.16.5.55,192.168.4.8,10.0.1.1,172.16.7.8,192.168.5.2,10.0.2.3,172.16.8.45,192.168.6.7,10.0.3.5,172.16.9.20,192.168.7.11,10.0.4.9,172.16.10.10,192.168.8.4,10.0.5.2,172.16.11.14,192.168.9.6,10.0.6.3,172.16.12.17,192.168.10.9,10.0.7.8,172.16.13.22,192.168.11.10,10.0.8.15,172.16.14.30,192.168.12.5,10.0.9.20,172.16.15.8,192.168.13.3,10.0.10.11,172.16.16.40,192.168.14.2,10.0.11.4,172.16.17.18,192.168.15.1,10.0.12.5"






###########################################################
