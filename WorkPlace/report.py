from fpdf import FPDF
class PDF(FPDF):
  def header(self):
      # Logo
      self.image("C:/Users/ronakkumar_sharma/Desktop/Reports/sanmina_logo.png",10,8,25)
      # Font
      self.set_font('helvetica', 'B', 20)
      # Title
      self.cell(0, 10, 'Title', ln=1, border=0,align='C')
#       Line break
      self.ln()

def create_file():
    # create FPDF object
    # Layout('P','L')
    from fpdf import FPDF

    # create FPDF object
    # Layout ('P','L')
    # Unit ('mm', 'cm', 'in')
    # format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=1,margin=15)
    # Add a page
    pdf.add_page()
    # specify font
    # fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
    # 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
    pdf.set_font('helvetica', '', 20)

    # Add text
    # w = width
    # h = height
    # txt = your text
    # ln (0 False; 1 True - move cursor down to next line)
    # border (0 False; 1 True - add border around cell)

    for i in range(1,50):
        # pdf.cell(30, 10, 'Ronak!', ln=0, border=1)

        pdf.cell(0,10,f'This is a line {i} : D',ln=1)
    pdf.cell(0, 280, '', ln=0, border=1)

    pdf.output("C:/Users/ronakkumar_sharma/Desktop/Reports/myfile1.pdf")


