import aspose.pdf as ap

input_pdf = "1_Introduction_to_ML_Biwei_Huang.pdf"
output_tex = "1_Introduction_to_ML_Biwei_Huang.tex"

# Open PDF file
document = ap.Document(input_pdf)

# Create an object of LaTeXSaveOptions class
saveOptions = ap.LaTeXSaveOptions()

# Save PDF as TEX
document.save(output_tex, saveOptions)