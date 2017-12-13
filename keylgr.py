import Tkinter as tk

def show_key(event):
	'''show event.keycode, event.keysym, event.char results'''
	if event.char == '0xff09':
		msg = 'Normal Key %r' % event.char
	elif len(event.char) == 1:
		msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
	else:
		msg = 'Special Key %r' % event.keysym
	print(msg)
	if event.keysym == 'Escape':
		root.destroy()
			
root = tk.Tk()
print("Press a key (Escape key to exit): ")
root.bind_all('<Key>', show_key)
# don't show the tk window
#root.withdraw()
root.mainloop()
