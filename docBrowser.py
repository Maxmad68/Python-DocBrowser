#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import imp
import pkgutil

from Tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *
from tkFileDialog import askopenfilename
import tkMessageBox

import os
import sys
import textwrap

class Unexisting():
	pass
	
class ImageDatas:
	"""
	Defines all small icons for classes, modules, functons, methods and constants
	"""
	classImageData = '''R0lGODdhEAAQAOYAAAAAAAAaSgklUBYtVxcvWhovWB0zXB83YiM6Zyg/bSpAbDNKd0hhkiRq0FZr
lidszytsz1RtnTNv0FpvmF5ymzdz0D11z0F1z113qkV51GV7pkt81Ft9vE2A1YCA/1SB1WKEw1uF
1luG2F6I2V2L0XSMu2WN2WiN1WmP2nCPy3WPwm+Q0GyS3HKT1HyTwGuU4XKW3HuWy3eY12yZ73SZ
3nmb3YCb0Hqc4X6c1YCf3H6g33Si6Iui6IOj3oOj4omn4oqp5JGu5JKv6Jax5pO095a07Zu15py3
6J646KK656O866m/6qnA6////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAkKAE4ALAAAAAAQABAAAAe9gE6Cg4SFgyY3PoqLijQmh0RKTEuUlUxKRI9OMEZJRkhKoUpIRkpG
MII1pEZGLhQUJUZHsjWpQ7caAg4UAxNBt7VONEFCMQElRUUqBzZCQTSCMEBAGAo9QD0/ONlAqE4s
ihELOT3lij0+LIIsOj4YBjWKMgwpPjrqTig1NysFDC0tGBBocaMGCkEmaMCgwQGBAgUJQCh0hJCF
RRYnOHA4cZGFphAzTIhk8eKFR5EzQgwKMaJliJctXRqaWSgQADs='''
	moduleImageData = '''R0lGODdhEAAQAMQAAAAAACQkJDY2NlVVVVpaWmRkZG5ubnR0dHl5eYKCgouLi5SUlJycnKOjo6ys
rLKysru7u8TExMnJydDQ0P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkK
ABUALAAAAAAQABAAAAWTYCWOZDkyTvqsa8qckTRJdD1Hb+VIEPNEwEjv5xDtGACEEBJZABKRog4n
IDgg2EJAETU2CwcFllEoQKUNiMKwKDwghwQCAWmI0oqCg9BwDBoHdHYVDQ8KBA9xbQ8GBw+DhYcP
CwMDCQ9gjyIoCX8NAwIoBQYOgwwNCwkNDQqqDQkKDTkoq7W2fTkVDLu8vbsmwCUhADs='''
	functionImageData = '''
R0lGODdhEAAQAOYAAAAAABdJXCpSZDJkeTZofDpqfkNrfUFugUJyhmSSpVSVsGGYr1uZs1ehv2mj
uiukzyam0Dem0Dym0HSmuyupz0Gpz0Op1HirwEut1FSt1Fatz1+tzXKtxYCtwVmu1YSxxVuy1V20
2WS22V250WW523S56Gu623O93Hi/3nbA3nvB3nTD43zE4YPE3oTF4IvF3YjH4GzI74TJ5ozK45PN
5YrP65nP5ZfR6pvS6J7S56HS56PU6KnX65zY8arY7JPZ967e8oD//////wAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAkKAEMALAAAAAAQABAAAAe1gEOCg4SFgyIsLi0uiosuKSKHPzs8lT5AQJU7P5FDJzo6OTk7Nh0f
oqEngio4NDY2OAkBCTQ5NDgqgig0vDQ3BhM9vTQogic0MzQvCQIGF8jJqp4zLdQLAggcMy4wM9Im
jIsyBw41LY4mgiYsKu0qBQwy7izpQyYqKSf58Cwn+ir1SOTzd4IAgxUET3QiYaJhwwEKVjg0QUIQ
iBgiSGhssIEiCRExQAwCEaJkiI8mQ4g0xJJQIAA7'''
	methodImageData = '''
R0lGODdhEAAQAOYAAAAAAAA4TC9ZazRecTRhdDtkdzZmez5qfTtrgEBrfT9whT9yiERyhUd7kUt7
j0t9klJ+kUuBl1ODmFaDlliFmFSIn02KoluMoVWRqlyXr2GXrlaYsmKctGudsl6hvCukz2CkwG2k
uyam0Dem0Dym0HWovSupz0Kpz0Op1Eyqz1Os03asw0yu1Vmu1Vuy1l202GS22IW3zIa4zF250Wa5
2nS56Gu623O93Xi/3XbA3nvB3nXC4YLD33vE44TE4I/E2ZDF2mzI74TJ5pPJ3ozL5JXN447P6Z7S
56HS55PT7JvT6qLV6ajW6qPY7ZTZ94D//////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAkKAFEALAAAAAAQABAAAAe6gFGCg4SFgzA9PoqLijkwh05LTJOUk0tOj1E3SEtHS02dn0tIRzeC
OkpFqjJASkMxP0dKOoI4Sh0TFAMFHRAEAiVKpppJFwErRBDHRBIHRcM3RhcOREkdDNUhCUTDNkQV
Dz5CGgw8QhwHPjaCNkIVDT1CGQo65wjq7D0RCzk9GAb9MhDosS4KjB0bMNzY4cHCQhAWctAQRMOG
xYsYLU6M4iJIRRogbYAEGcTFIBcvUL5YuRKlSUMwCQUCADs='''
	attributeImageData = '''
R0lGODdhEAAQAOYAAAAAACJHADFRETVXDzxcHkJhJUVlKE5wLVV2NVN4L1p7O12BPFyDNmODRWGF
P2aJRWuNS2qPRnOWU26YRnWYVHyaYH2fXXmhUn+mWYCoWYqsaIGtVYmvZZO0cpe5dpO7bY+8Y4y9
W43AXJjNY5zNa6bOgIbPK4rPQYTQJojQN4jQPKbQfIvRXaLRXaPTdI3UQ4/USY/UUpHVVZLVTZbV
WpnWXJ7WaKzWg5fYW5rZX57ZZaDbZ6Lba6bcc7DdhKnedKvee6rgdK/gg6Xha63ie7Dif7LihLbi
i7vklL/mmcLmnsTnoaLodLnoi73olMHom8Xoo8nqqbnthsjto6zvbMXymcj1nMP3k4D/gP///wAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAkKAFoALAAAAAAQABAAAAfBgFqCg4SFgzpERkKLjEI/OodXUFGUlZRQV5BaP0tLSlBToVNQn0o9
gkBPSKodFRUeSEmrQKhISEcNBRYSARpOtrSbSE4lCjdWVRQNtkinWj1HR0Y+Kx8cBhDRR848RkZA
EggRGAsP3kY8gjxARhkDLkZSFw5FQEDpWutEFwQkPSACFvSwh0/Hjx8kEhA4wGCCgA1BHgnSwaOi
jRAhbPAQMaKiphpUdOzgMWQIjx0mdVCpMahGjhw1Yr6UydKQTUKBAAA7'''
	constantImageData = '''
R0lGODdhEAAQAOYAAAAAAHsr0Hwrz4A30IA80IJBz05DX1BEY4ZF1IZJ1FVKZFlNaopO1GhTh4tT
1ZFV2WtZgpFa1o9b2I1c03Rdk3teopNf2H9gqHphm35joYFjqnpklpZl2oBmo4dmtJhn2oZqrJds
z5ds0Jts26Rs74tttJpu04ZvpJlxzp9x26F03aR63aB70aZ74al+4Zx/woCA/6mC3auE4aaG0a6I
4qKL6LmL6LGN47WS472T97KU3LmW5ruc5r2e6L+h6b+i58Gj6cWp6////wAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAkKAEMALAAAAAAQABAAAAeygEOCg4SFgx8tMoqLii0fgxw5QEGUlZRAORyCKjw/PJ8+PUA9PD48
KoIrpJ88Oq44nz0rqTs4OLUnLye3t7NDKjg3ODMbCxAKLzfCqEMpNzTQHRgYIDEyNDcpgiOKMSwU
GRQlMtYyI9suKy0aBg0HFSvpLudDIysqLSgVHhcuKv8r6H1QkUKFiRAiTBBMUVDTEA4jIkqcGNFh
BBIcPnzgwFHjRhIRBkWwQLKkyZCGUhIKBAA7'''

def getAttributesForSource(sourcecode,includingHidden=True):
	attributes = []
	lines = sourcecode.replace('\t','').replace('\n\n','\n').split('\n')
	for line in lines:
		try:
			if '=' in line:
				declarators = line.split('=')[0]
				for dec in declarators.replace(' ','').split(','):
					if 'self.' in dec:
						attribute = dec.split('.')[1]
						attribute = attribute.split('[')[0]
						if '(' in attribute:
							continue
						if attribute not in attributes:
							attributes.append(attribute)
		except:
			continue
	return filter(lambda s:(s[0] != '_') if not includingHidden else True,attributes)


class DocBrowser(object):
	def __init__(self,modulename=__builtins__,winInstance=None):
		try:
			if isinstance(modulename, basestring):
				if os.path.isfile(modulename):
					file_ = modulename
					modulename = '.'.join(os.path.split(modulename)[-1].split('.')[:-1])
					module = imp.load_source(modulename,file_)
				else:
					module = imp.load_module(modulename,*imp.find_module(modulename))
			elif inspect.ismodule(modulename):
				module = modulename
				modulename = module.__name__
		except Exception as e:
			tkMessageBox.showerror("Error", e)
			sys.exit()

		
		root = Toplevel(winInstance)
		root.geometry('1000x750')
		root.title(modulename)

		objectsForSubmenus = {}

		getImage = lambda data : PhotoImage(data=data)

		classImage = getImage(ImageDatas.classImageData)
		methodImage = getImage(ImageDatas.methodImageData)
		functionImage = getImage(ImageDatas.functionImageData)
		attributeImage = getImage(ImageDatas.attributeImageData)
		moduleImage = getImage(ImageDatas.moduleImageData)
		constantImage = getImage(ImageDatas.constantImageData)


		tree = ttk.Treeview(root)

		moduleSubmenu = tree.insert("" , 0,    text=modulename,image=moduleImage)
		objectsForSubmenus[moduleSubmenu] = module

		tree.insert("", 1, "modules", text="Modules")
		
		tree.insert("", 2, "submodules", text="Submodules")

		tree.insert("", 3, "classes", text="Classes")

		tree.insert("", 4, "functions", text="Functions")

		tree.insert("", 5, "methods", text="Methods")

		tree.insert("", 'end', "constants", text="Constants")
		
		def getImageFor(obj):
			if inspect.isclass(obj):
				return classImage
			elif inspect.ismodule(obj):
				return moduleImage
			elif inspect.ismethod(obj):
				return methodImage
			elif inspect.isfunction(obj):
				return functionImage
			else:
				return constantImage

		def getEntriesForClass(item,obj):
			classesSubitem = tree.insert(item, 2, "", text="Classes")

			functionsSubitem = tree.insert(item, 3, "", text="Functions")

			methodsSubitem = tree.insert(item, 4, "", text="Methods")
			
			instMethodsSubitem = tree.insert(item, 5, "", text="Instance Methods")
			
			for name, obj in inspect.getmembers(obj):
				if '__' in name:
					if inspect.ismethod(obj):
						submenu = tree.insert(instMethodsSubitem, "end", "", text=name,image=methodImage)
						objectsForSubmenus[submenu] = obj
					continue
					
				if inspect.isclass(obj):
					if obj.__module__ == module.__name__:
						submenu = tree.insert(classesSubitem, "end", "", text=name,image=classImage)
						getEntriesForClass(submenu,obj)
					
					else:
						continue
						
				elif (inspect.ismethod(obj) or 'builtin_function_or_method' in str(type(obj))) and '__' not in name:
					submenu = tree.insert(methodsSubitem, "end", "", text=name,image=methodImage)
				elif inspect.isfunction(obj):
					submenu = tree.insert(functionsSubitem, "end", "", text=name,image=functionImage)
				else:
					submenu = tree.insert(item, 'end', '', text=name,image=constantImage)
				
				objectsForSubmenus[submenu] = obj
				
				
				
				

		for name, obj in inspect.getmembers(module):
			if '__' in name:
				continue
				
				
			if inspect.isclass(obj):
				if obj.__module__ == module.__name__:
					submenu = tree.insert('classes', "end", "", text=name,image=classImage)
					getEntriesForClass(submenu,obj)
				else:
					continue
					
			elif inspect.ismethod(obj) or 'builtin_function_or_method' in str(type(obj)):
				submenu = tree.insert('methods', "end", "", text=name,image=methodImage)
			elif inspect.ismodule(obj):
				submenu = tree.insert('modules', "end", "", text=name,image=moduleImage)
			elif inspect.isfunction(obj):
				submenu = tree.insert('functions', "end", "", text=name,image=functionImage)
			else:
				submenu = tree.insert("constants", 'end', '', text=name,image=constantImage)
			
			objectsForSubmenus[submenu] = obj


		try:
			for importer, modname, ispkg in pkgutil.iter_modules(module.__path__):
				submenu = tree.insert('submodules', "end", "", text=modname,image=moduleImage)
				obj = importer.find_module(modname).load_module(modname)
				objectsForSubmenus[submenu] = obj
		except:
			pass

		
		def openDetails(event):
			item = tree.focus()
			obj = objectsForSubmenus.get(item)
			if obj:
				if inspect.ismodule(obj):
					DocBrowser(obj,winInstance)
					
		def showSource(event):
			item = tree.focus()
			obj = objectsForSubmenus.get(item)

			
			docView.delete('showSource.first','showSource.last')
			docView.insert('end','Source:\n','sourceTitle')
			try:
				docView.insert('end', textwrap.dedent(inspect.getsource(obj)),'sourceCode')
			except:
				docView.insert('end',obj,'sourceCode')
			docView.insert('end','\nHide Source','hideSource')
			
			
		def hideSource(event):
			
			docView.delete('sourceCode.first','sourceCode.last')
			docView.delete('hideSource.first','hideSource.last')
			docView.delete('sourceTitle.first','sourceTitle.last')

			docView.insert('end','Show Source','showSource')
			
			

		docView = Text(root,font = ("Courier", 15))
		docView.bind("<Key>", lambda e: "break")
		
		docView.pack(expand=True,fill=BOTH,side=RIGHT)

		#Create tags
		docView.tag_config('objName',font = ("Courier", 15, 'underline','bold' ))

		docView.tag_config('noDoc',font = ("Courier", 15, 'italic' ))
		
		docView.tag_config('inheritsClass',font = ("Courier", 15, 'italic' ))
		
		docView.tag_config('openModuleTag', foreground="blue")
		docView.tag_bind('openModuleTag', '<Button-1>', openDetails)
		
		docView.tag_config('sourceTitle',font = ("Courier", 15, 'underline','bold' ))
		
		docView.tag_config('showSource',font = ("Courier", 15,  'underline','italic'))
		docView.tag_bind('showSource', '<Button-1>', showSource)
		
		docView.tag_config('hideSource',font = ("Courier", 15,  'underline','italic'))
		docView.tag_bind('hideSource', '<Button-1>', hideSource)
		
		docView.tag_config('sourceCode',font = ("Courier", 12),background="#e6e6e6")
		
		

		def openDocFor(obj,name):
			doc = inspect.getdoc(obj)

			
			docView.delete('1.0',END)
			
			imageTypeObj = getImageFor(obj)
			
			docView.image_create('end', image=imageTypeObj)
			docView.insert('end',' '+name,'objName')
			
			if inspect.isclass(obj):
				if obj.__bases__:
					docView.insert('end','\nInherits from ')
					docView.insert('end',','.join(map(lambda t:t.__name__,obj.__bases__)),'inheritsClass')
				else:
					docView.insert('end','\nDoesn\'t inherits from any class')
			
			docView.insert('end','\n\n\n')
			
			

			if doc:
				docView.insert('end', doc)
			else:
				docView.insert('end','No Documentation',('noDoc'))
				
			if inspect.ismethod(obj) or 'builtin_function_or_method' in str(type(obj)) or inspect.isfunction(obj):
				docView.insert('end','\n\n\n\n\n')
				try:
					docView.insert('end','Arguments:\n','objName')

					args = inspect.getargspec(obj)
					
					arguments = ', '.join(map(lambda t:(str(t[0])+'='+repr(t[1])) if t[1] != Unexisting else str(t[0]),zip(args.args,[Unexisting]*(len(args.args)-len(args.defaults))+list(args.defaults))) if args.defaults else args.args)
					
					howToUse = '%s(%s%s%s)'%(obj.__name__,arguments,(',*%s'%args.varargs) if args.varargs else '',(',**%s'%args.keywords) if args.keywords else '')
					docView.insert('end',howToUse)
				except:
					pass
				
				docView.insert('end','\n\n\n\n')
				docView.insert('end','Show Source','showSource')
				
			elif inspect.isclass(obj) and hasattr(obj,'__init__'):
				try:
					args = inspect.getargspec(obj.__init__)
				except:
					pass
				else:
				
					source = inspect.getsource(obj)
					if source.count('\n') < 500:
						attributs = getAttributesForSource(source,False)
						if attributs:
							docView.insert('end','\n\n\n\n\n')
							docView.insert('end','Attributes:','objName')
							docView.insert('end','(estimated)\n')
							
							for attribut in attributs:
								docView.insert('end','\t')
								docView.image_create('end', image=attributeImage)
								docView.insert('end',attribut)
								docView.insert('end','\n')
							
					docView.insert('end','\n\n\n\n\n')
					docView.insert('end','Arguments:\n','objName')

					
					arguments = ', '.join(map(lambda t:(str(t[0])+'='+repr(t[1])) if t[1] != Unexisting else str(t[0]),zip(args.args,[Unexisting]*(len(args.args)-len(args.defaults))+list(args.defaults))) if args.defaults else args.args)
					
					howToUse = '%s.%s(%s%s%s)'%(obj.__name__,obj.__init__.__name__,arguments,(', *%s'%args.varargs) if args.varargs else '',(', **%s'%args.keywords) if args.keywords else '')
					docView.insert('end',howToUse)
				
			elif inspect.ismodule(obj):
				docView.insert('end','\n\n\n\n\n')
				docView.insert('end','Open','openModuleTag')
			
			else:
				docView.insert('end','\n\n\n\n')
				docView.insert('end','Show Source','showSource')
				
			


		def select(event):
			item = event.widget.focus()
			obj = objectsForSubmenus.get(item)
			name = (tree.item(item)['text'])
			if obj:
				openDocFor(obj,name)
				

					
		tree.bind("<<TreeviewSelect>>", select)
		tree.bind("<Double-Button-1>", openDetails)
		tree.pack( fill=Y,side=LEFT)

		root.mainloop()
		
		
def openDocForModule(*args):
	def browse(*args):
		modulename = module.get()
		subwindow.destroy()
		DocBrowser(modulename,master)
		
	def chooseFile(*args):
		filename = askopenfilename()
		module.delete(0,END)
		module.insert(0,filename)
	
	subwindow = Toplevel(master)
	subwindow.title('DocBrowser')
	
	lbl = Label(subwindow,text='Module:')
	lbl.grid(row=0,column=0)
	
	module = Entry(subwindow)
	module.grid(row=0,column=1)
	
	chooseFileButton = Button(subwindow,text='File',command=chooseFile)
	chooseFileButton.grid(row=0,column=3)
	
	validateButton = Button(subwindow,text='Browse',command=browse)
	validateButton.grid(row=1,column=0,columnspan=4)
	
	subwindow.bind('<Return>', (lambda e, validateButton=validateButton: validateButton.invoke()))
	
	subwindow.mainloop()

master = Tk()
master.withdraw()


menubar = Menu()

menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=menu)
menu.add_command(label="Open",command=openDocForModule)
menu.add_command(label="Open __builtins__",command=lambda *args: DocBrowser(__builtins__))


master.config(menu=menubar)


if '--help' in sys.argv or '-h' in sys.argv:
	print 'DocBrowser, by Maxime MADRAU'
	print
	print 'Usage:'
	print '  docbrowser <file-or-module>'
	sys.exit()

if len(sys.argv) > 1:
	mod = sys.argv[1]
	DocBrowser(mod,master)
else:
	openDocForModule(0)