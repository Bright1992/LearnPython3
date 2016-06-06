#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Chain:
	def __init__(self,path=''):
		self._path=path
		self._cmd="GET "+path

	def __str__(self):
		return self._cmd

	def __getattr__(self,attr):
		if attr=='users':
			def users(user):
				return Chain("%s/users/%s"%(self._path,user))
			return users
		return Chain("%s/%s"%(self._path,str(attr)))

if __name__=='__main__':
	print(Chain().users("Bright").irobot)