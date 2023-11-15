import string 
import secrets

# Hidden file
from message import message


message = message.lower()
for i in message:
	if ord(i) not in range(97,123):
		message = message.replace(i, "")

alphabet = string.ascii_letters
key = []

while True:
	if len(key) == 26:
		break
	char = "".join(alphabet[secrets.randbelow(len(alphabet))] for _ in range(3))
	if char not in key:
		key.append(char)

alphabet = string.ascii_lowercase
dic = {term : char for term, char in zip(alphabet, key)}

cipher = ""
for i in message.lower():
	if i in alphabet:
		cipher += dic[i]
	else:
		cipher += i 

print(f"{cipher = }")
# cipher = 'ZJjczesjQzxwcdAeyuTDNymWaDIzxwoePeyudmmcdAoePPWSxCeoskPWSTDNZJjTDNxCeTDNZJjymWczesjQZJjeyudmmgDfzxwZJjPWSoePjyLgDfTDNdmmymWHMFymWykbgDfczesjQzxwcdAeyuTDNZJjczeaDIZJjczeNLZdmmZJjsjQdmmxCeczeZJjTDNPWSymWykbeyuNpYoePZJjczeTDNgDfgrNTDNoePzxwgDfzxwgDfeyuNpYoePsjQgDfHMFNLZZJjTDNdmmTDNdmmgDfsjQZJjeyudmmgDfzxwTDNgDfgrNTDNZJjczeoePHMFgDfykbZJjczegDfHMFjyLoePczeczegDfzxwNLZZJjTDNdmmTDNdmmgDfdmmgDfNpYeyuymWykboePDJrgDfcdATDNdmmgDfxCeczeZJjTDNPWSjyLoePcdAoskgDfPWSZJjczeaDINpYgDfNpYgDfTDNTDNgDfzxwPWSTDNdmmgDfjyLymWPWSTDNsjQymWjyLjyLymWczeeyuoePZJjzxwPWSymWykbNpYgDfTDNTDNgDfzxwPWSTDNzxwZJjeyuNpYgDfTDNPWSymWykbNpYgDfTDNTDNgDfzxwPWSjyLZJjgrNTDNxCezxwgDfPWSymWykbTDNdmmgDfoePoskymWpcAgDfoePczeHMFPWSymWykbymWzxwTDNdmmTDNdmmgDfzxwgDfsjQgDfZJjpcAgDfzxwHMFgDfsjQZJjeyudmmgDfzxwPWSTDNdmmgDfTDNgDfgrNTDNoskcdAeyugDfzxwykbymWzxwjyLZJjczeaDITDNdmmgDfZJjczepcAgDfzxwPWSgDfPWSxCeoskPWSTDNZJjTDNxCeTDNZJjymWczeeyuzxwymWsjQgDfPWSPWSTDNymWgDfgrNTDNzxwoePsjQTDNTDNdmmgDfymWzxwZJjaDIZJjczeoePNpYjyLgDfPWSPWSoePaDIgDfTDNdmmgDfykbNpYoePaDIZJjPWSgDfpcAgDfzxwcdATDNdmmZJjczeaDIoePykbTDNgDfzxwTDNdmmZJjPWSTDNgDfzxwoePTDNymWPWSoePxCezxwxCePWS'
