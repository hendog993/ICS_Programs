from tkinter import Tk, Label, Entry, Text , Button

# Testing right now.
# try:
# 	import urlparse
# except ModuleNotFoundError:
# 	import urllib.parse as urlparse
# from office365.runtime.auth.authentication_context import AuthenticationContext
# from office365.sharepoint.client_context import ClientContext
# from office365.sharepoint.file import File

# Enter required values into a simple GUI
# Press enter, save the values to a text file
# Send that data to the online excel database

def main():
	GUI.run()


class GUI:
	""" Creates a GUI instance that opens during every print. """

	def run():
		GUI.root.mainloop()

	def reader():
		# Fetches the data from the entry boxes,
		# Clears the entry boxes
		# Returns the relevent information in a list.

		values = []
		for x in GUI.entries:
			values.append(x.get())
		for x in GUI.entries:
			x.delete(0,"end")
		return values

	def writer(values):
		# Writes the values to a file at this point.
		with open('printerlog.txt','w') as master:
			for x in values:
				master.write(x)
				master.write("\n")
			master.write("\n")
			master.close()

	def read_and_write():
		var = GUI.reader()
		GUI.writer(var)
		pass

	def post_data():
		# office365 validation, post to lowest column.
		# Hold this data in a seperate secure file. Use json loading to pull.
		url = 'https://www.dropbox.com/login'
		username = 'yourusername'
		password = 'yourpassword'
		relative_url = '/sites/documentsite/Documents/filename.xlsx'
		pass

	def submit_button():
		# Grab data from fields
		# Store in a text file??
		# Post online.
		# Clear contents in entry fields.
		var = GUI.fetch_data()
		print(var)
		pass


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

	filamentType = Label(root,text = "Filament").grid(row=3, column = 0)
	filamentEntry = Entry(root, width=30)
	filamentEntry.grid(row=3, column =1)

	lengthLabel = Label(root, text="Length (m)").grid(row=4, column=0)
	lengthEntry = Entry(root, width=30)
	lengthEntry.grid(row=4, column=1)

	staffHelperLabel = Label(root, text="Staff Helper").grid(row=5, column=0)
	staffHelperEntry = Entry(root, width=30)
	staffHelperEntry.grid(row=5, column=1)

	descriptionLabel = Label(root, text="Description").grid(row=6, column=0)
	descriptionEntry = Entry(root, width=30)
	descriptionEntry.grid(row=6, column=1)

	submit_button = Button(root, text="Submit", command=read_and_write).grid(row=6, column=2)

	entries = [printerEntry, studentNameEntry, studentnetIDEntry, \
				filamentEntry,lengthEntry,  staffHelperEntry,
				descriptionEntry]

	pass

if __name__ == "__main__":
	main()
