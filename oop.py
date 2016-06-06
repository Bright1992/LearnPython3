#!/usr/bin/python3
#-*- coding:utf-8 *-*

class Sensor:
	amount=0		#static member
	__slots__=()
	def __init__(self):
		Sensor.amount+=1
		self.__data=[]
		self.__type=""
	#	self.data=[]
		self._data=[]
	#def getdata(self):
	#	return self.data

	#BY using @property Decorator, private members can be avoided and getter/setter func can be ommited.
	@property
	def data(self):
		return self._data

	@data.setter
	def data(self,value):
		if not isinstance(value,list):
			raise ValueException("data must be a list")
		self._data=value
	
	#for len()
	def __len__(self):
		return len(self.data)
	#for str()
	def __str__(self):
		return "%s Object"%self.__class__

	#for for i in xx(where iterator is needed)
	def __iter__(self):
		return (x for x in self.data)

	#use object as a list:
	def __getitem__(self,n):
		if(isinstance(n,int)):			#subscript is Integer
			if n>=len(self.data):
				raise IndexError("Index out of range")
			return data[n]
		elif(isinstance(n,slice)):		#subscript is Slice
			n1=n.start
			n2=n.stop
			if n1 is None:
				n1=0
			if n1>len(self.data):
				return []
			if n2>len(self.data):
				n2=len(self.data)
			return [self.data[x] for x in range(n1,n2)]		#haven't considered negative subscript yet..

	#in case undecleared members are accessed:
	def __getattr__(self,attr):
		if attr=='sname':
			return self.__class__

	#use object as a function, i.e., object is a instance of Callable
	def __call__(self,*args):
		return ["%s:%s"%(self.__class__,str(x)) for x in args]




	def collect(self):
		pass

class Gyro(Sensor):
	__slots__=('getmisc','misc','name','__type','__data','_data')		#limitation of what attributes that can be added statically OR dynamically
	def __init__(self):
		#super(Gyro,self).__init__()			#invoke constructor of super class
		Gyro.amount+=1
		self.__type='Gyro'
		self.__data=[0,0,0]
		self._data=[0,0,0]
		#self.data=[0,0,0]

	#must overwrite this. Because in super class, variable self.__data is resolved to _Sensor__data, while we mean _Gyro__data here.
	#def __len__(self):				
	#	return len(self.__data)

	#OR if you want to omit the overwriting, just don't use private member.

	#def getdata(self):
	#	return self.__data

	def collect(self):
		pass

class Thermometer(Sensor):
	def __init__(self):
		Thermometer.amount+=1
		self.__type='Thermometer'
		self.__data=[0]
		self._data=[0]

	#def getdata(self):
	#	return self.__data

	def collect(self):
		pass


if __name__=='__main__':
	#print(dir('Gyro'))
	print(Gyro.__slots__)
	s=Gyro()
	s.misc=1			#add member to an instance DYNAMICALLY!
	try:
		s.price=1			#error, because 'slot' is not contained in variable Gyro.__slots__
	except AttributeError:
		print("Attribute Error, 'price' isn't contained in __slots__")

	print("sname:%s"%s.sname)

	from types import MethodType
	def getmisc(self):
		return self.misc
	s.getmisc=MethodType(getmisc,s)		#bind function to an instance DYNAMICALLY!


	def cls_func(self):
		print(self)
	Gyro.cls_func=cls_func				#bind function to a class DYNAMICALLY!
	s.cls_func()

	print("s.getmisc:%s"%s.getmisc())
	s2=Gyro()
	t=Thermometer()
	#print(s.getdata(),len(s))

	s.data.append(1)		#@property Decorator!

	print(s.data,len(s))
	setattr(s,'name','myGyro')
	print(getattr(s,'name'),s.name)
	fn=getattr(s,'__len__')
	print("fn():%s"%fn())
	print(Gyro.amount,Thermometer.amount,Sensor.amount)
	print(len(t))

	from collections import Iterator 	
	if isinstance(s,Iterator):
		for i in s:
			print("Iterator:",i)
	try:
		print(s[5])
	except IndexError as e:
		print(e)

	print(s[3:6])

	print(s('Bright','Joshua'))