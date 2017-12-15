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
		if event.keysym == 'Up':
			with open("strcmd.txt","r+") as f:
				lstline = f.readline()
			print(lstline[-1])
		
					
		
root = tk.Tk()
app = MyApp(root)
root.mainloop()
