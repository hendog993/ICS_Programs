from tkinter import Tk, Label, Entry, Text , Button

# Enter required values into a simple GUI
# Press enter, save the values to a text file
# Send that data to the online excel database

def main():
	GUI.run()


class GUI:
	""" Creates a GUI instance that opens during every print. """

	def run():
		GUI.root.mainloop()


	def fetch_data():
		# Fetches the data from the entry boxes,
		# Clears the entry boxes
		# Returns the relevent information in a list.

		values = []
		for x in GUI.entries:
			values.append(x.get())
		for x in GUI.entries:
			x.delete(0,"end")

		return values

	def post_data():
		pass



	def submit_button():
		# Grab data from fields
		# Store in a text file??
		# Post online.
		# Clear contents in entry fields.
		var = GUI.fetch_data()
		print(var)


	root = Tk()
	root.geometry('500x200')

	printerName = Label(root,text = "Printer name").grid(row=0, column = 0)
	printerEntry = Entry(root, width=30)
	printerEntry.grid(row=0, column =1)

	student_Name = Label(root,text="Student name").grid(row=1, column = 0)
	studentNameEntry = Entry(root, width=30)
	studentNameEntry.grid(row=1, column =1)

	studentnetId = Label(root,text = "Net ID").grid(row=2, column = 0)
	studentnetIDEntry = Entry(root, width=30)
	studentnetIDEntry.grid(row=2, column =1)

	filamentType = Label(root,text = "Filament(m)").grid(row=3, column = 0)
	filamentEntry = Entry(root, width=30)
	filamentEntry.grid(row=3, column =1)

	lengthLabel = Label(root, text="Length").grid(row=4, column=0)
	lengthEntry = Entry(root, width=30)
	lengthEntry.grid(row=4, column=1)

	staffHelperLabel = Label(root, text="Staff Helper").grid(row=5, column=0)
	staffHelperEntry = Entry(root, width=30)
	staffHelperEntry.grid(row=5, column=1)

	descriptionLabel = Label(root, text="Description").grid(row=6, column=0)
	descriptionEntry = Entry(root, width=30)
	descriptionEntry.grid(row=6, column=1)

	submit_button = Button(root, text="Submit", command=submit_button).grid(row=6, column=2)

	entries = [printerEntry, studentNameEntry, studentnetIDEntry, \
				filamentEntry,lengthEntry,  staffHelperEntry,
				descriptionEntry]

	pass

if __name__ == "__main__":
	main()
