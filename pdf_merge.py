import tkinter as tk
from tkinter import filedialog
import PyPDF2

# Create the GUI window
window = tk.Tk()
window.title("PDF Merger")

# Create a function to merge PDFs
def merge_pdfs():
    # Get the file path of the PDF to merge
    file_path = filedialog.askopenfilename()

    # Get the file path of the PDF to add
    add_path = filedialog.askopenfilename()

    # Get the file path to save the merged PDF
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf")

    # Open the PDF files to merge
    with open(file_path, "rb") as file, open(add_path, "rb") as add:
        # Create a PDF reader object for each file
        file_reader = PyPDF2.PdfReader(file)
        add_reader = PyPDF2.PdfReader(add)

        # Create a PDF writer object to write the merged PDF
        writer = PyPDF2.PdfWriter()
        # Add the pages from the PDF to merge
        for page_num in range(len(file_reader.pages)):
            writer.add_page(file_reader.pages[page_num])

        # Add the pages from the PDF to add
        for page_num in range(len(add_reader.pages)):
            writer.add_page(add_reader.pages[page_num])

        # Write the merged PDF to the save path
        with open(save_path, "wb") as output:
            writer.write(output)

    # Show a success message
    success_label = tk.Label(window, text="PDFs merged successfully!")
    success_label.pack()

# Create a button to merge PDFs
merge_button = tk.Button(window, text="Merge PDFs", command=merge_pdfs)
merge_button.pack()

# Run the GUI window
window.mainloop()
