import Tkinter as tk


class MyApp(object):
	def __init__(self, master):
		self.text = tk.Text(master)
		self.text.bind('<Key>', self.show_key)
		self.text.pack()
		self.text.focus()

	def callback(self, event):
		print('{k!r}'.format(k = event.char))

    	def show_key(self, event):
		if event.char == event.keysym:
			msg = 'Normal Key %r' % event.char
		elif len(event.char) == 1:
			msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
		else:
			msg = 'Special Key %r' % event.keysym
		print(msg)
		if event.keysym == 'Escape':
			root.destroy()
		
	def record(self, cmd):
		with open("strcmd.txt","a+") as f:
			f.write(cmd)
	def keyact(self, event):
		i = 0
		while( event.keysym == 'Up' or event.keysym == 'Down'):
			if event.keysym == 'Up':
				keyup(self, i)
			elif event.keysym == 'Down':
				keydown(self, i)
			else:
				break

	def keyup(self, i):
		with open("strcmd.txt","r+") as f:
				lstline = f.readline()
			i -= 1
			print(lstline[i])
	def keydown(self, i):
		with open("strcmd.txt","r+") as f:
				lstline = f.readline()
			i += 1	
			print(lstline[i])
				
		
root = tk.Tk()
app = MyApp(root)
root.mainloop()