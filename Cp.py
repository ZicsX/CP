import re

def applyDiscount(sentence, discount):
	prices = re.findall(r'\s+\$\d+', sentence)
	for i in range(len(prices)):
		price = float(prices[i].strip('$ '))
		discountPrice = format(price * (100 - discount) / 100, '.2f')
		sentence = sentence.replace(prices[i], '$'+str(discountPrice)+" ")

	return sentence.strip()

sentence = "duew$11mengf $8 $1"
discount = 7
print(applyDiscount(sentence, discount))