import re

def minusit(before,minusby): # input (1-num int,1-num int) both in range of [1,10]
	value = before - minusby
	if value < 0:
		value += 10
	else:
		value = value
	return value

def addtoit(before,addby): # input (1-num int,1-num int) both in range of [1,10]
	value = before + addby
	if value > 9:
		value -= 10
	else:
		value = value
	return value

def format(put): #format less-than-5-num number to 5-num | input "str"
	_put = "00000" + put
	return _put[len(_put)-5::1]

def transform(string,value):
	a,b,c,d = value//1000,(value%1000)//100,(value%100)//10,value%10
	_split = []
	for i in string:
		_split.append(i)
		####print(_split)
	for i in range(0,len(_split),4):
		_split[i] = str(addtoit(int(_split[i]),a))
	for i in range(1,len(_split),4):
		_split[i] = str(addtoit(int(_split[i]),b))
	for i in range(2,len(_split),4):
		_split[i] = str(addtoit(int(_split[i]),c))
	for i in range(3,len(_split),4):
		_split[i] = str(addtoit(int(_split[i]),d))

	_result_ = ""
	for i in _split:
			_result_ += i

	return _result_

def transback(string,value):
	a,b,c,d = value//1000,(value%1000)//100,(value%100)//10,value%10
	_split = []
	for i in string:
		_split.append(i)
		####print(_split)
	for i in range(0,len(_split),4):
		_split[i] = str(minusit(int(_split[i]),a))
	for i in range(1,len(_split),4):
		_split[i] = str(minusit(int(_split[i]),b))
	for i in range(2,len(_split),4):
		_split[i] = str(minusit(int(_split[i]),c))
	for i in range(3,len(_split),4):
		_split[i] = str(minusit(int(_split[i]),d))

	_result_d_ = ""
	for i in _split:
			_result_d_ += i

	_split_ = re.findall(r'.{5}',_result_d_)

	_result_ = ""
	for i in _split_:
		_result_ += chr(int(i))

	return _result_

while True:
	method = input("method:")
	if method in ["encode","en","e","1"]:
		sentence = input("content:")
		pw = input("4-number-length-password:")
		if len(pw) == 4:

			_split = []
			_result = []
			_result_ = ""
			for i in sentence:
				_split.append(i)
			for i in _split:
				_result.append(format(str(ord(i))))
			###print(_result)
			for i in _result:
				_result_ += i
			###print(_result_)
            
            #print("---------")
			print("--------",transform(_result_,int(pw)),"--------",sep="\n")
            #print("---------")

		else:
			print("not a proper password!")

	elif method in ["decode","de","d","2"]:###
		sentence = input("content:")
		pw = input("enter the password:")

		if len(pw) == 4:
			_result = []
			_result_ = ""
			for i in sentence:
				_result.append(i)
			for i in _result:
				_result_ += i

			print("--------",transback(_result_,int(pw)),"--------",sep="\n")

		else:
			print("not a proper password!")

	else:
		print("no such method")
		break
