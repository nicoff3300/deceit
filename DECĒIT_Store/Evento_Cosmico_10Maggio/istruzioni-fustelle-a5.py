from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = A5  # 148mm × 210mm

FONT_DIR = '/Users/nicoskolp/.agents/skills/canvas-design/canvas-fonts/'

BLACK = HexColor('#1a1a1a')
WHITE = HexColor('#ffffff')
ACCENT = HexColor('#d4a853')
GREY = HexColor('#999999')
LIGHT_GREY = HexColor('#f2f2f2')
DARK = HexColor('#0d0d0d')

c = canvas.Canvas('/Users/nicoskolp/Desktop/DECĒIT_MARKETING_AI/DECĒIT_Store/Evento_Cosmico_10Maggio/istruzioni-fustelle-A5.pdf', pagesize=A5)
c.setTitle('Disegna la tua T-shirt di carta — Istruzioni')
c.setAuthor('DECĒIT × COSMICO')

# === PAGE 1: FRONTE (title + visual) ===

# Background
c.setFillColor(WHITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Top accent bar
c.setFillColor(DARK)
c.rect(0, H - 8*mm, W, 8*mm, fill=1, stroke=0)

# Brand names
c.setFillColor(WHITE)
c.setFont('Helvetica', 7)
c.drawString(10*mm, H - 5.5*mm, 'DECĒIT')
c.drawRightString(W - 10*mm, H - 5.5*mm, 'COSMICO')

# Big title
c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 22)
c.drawCentredString(W/2, H - 42*mm, 'DISEGNA LA TUA')

c.setFont('Helvetica-Bold', 28)
c.setFillColor(ACCENT)
c.drawCentredString(W/2, H - 62*mm, 'T-SHIRT')

c.setFont('Helvetica-Bold', 22)
c.setFillColor(DARK)
c.drawCentredString(W/2, H - 80*mm, 'DI CARTA')

# Subtitle
c.setFont('Helvetica', 9)
c.setFillColor(GREY)
c.drawCentredString(W/2, H - 95*mm, 'Prendi una fustella, disegna, appendi.')

# Visual: T-shirt outline shape (simplified)
c.setStrokeColor(DARK)
c.setLineWidth(0.8)
c.setFillColor(HexColor('#f8f8f8'))
# Draw a stylized T-shirt shape as a visual element
shirt_w = 55*mm
shirt_h = 65*mm
shirt_x = W/2 - shirt_w/2
shirt_y = H - 145*mm

# T-shirt path
p = c.beginPath()
# Start at bottom left
p.moveTo(shirt_x + 5*mm, shirt_y)
# Bottom hem
p.lineTo(shirt_x + shirt_w - 5*mm, shirt_y)
# Right side
p.lineTo(shirt_x + shirt_w - 5*mm, shirt_y + 35*mm)
# Right sleeve
p.lineTo(shirt_x + shirt_w, shirt_y + 40*mm)
p.lineTo(shirt_x + shirt_w - 5*mm, shirt_y + 45*mm)
# Right shoulder line to collar
p.lineTo(shirt_x + shirt_w - 15*mm, shirt_y + 40*mm)
# Collar
p.lineTo(shirt_x + shirt_w - 15*mm, shirt_y + 50*mm)
p.lineTo(shirt_x + 15*mm, shirt_y + 50*mm)
# Left shoulder
p.lineTo(shirt_x + 15*mm, shirt_y + 40*mm)
# Left sleeve
p.lineTo(shirt_x + 5*mm, shirt_y + 45*mm)
p.lineTo(shirt_x, shirt_y + 40*mm)
p.lineTo(shirt_x + 5*mm, shirt_y + 35*mm)
# Close
p.lineTo(shirt_x + 5*mm, shirt_y)
p.close()
c.drawPath(p, fill=1, stroke=1)

# Small decorative dots inside shirt
c.setFillColor(ACCENT)
for i in range(3):
    cx = shirt_x + (i+1) * shirt_w/4
    c.circle(cx, shirt_y + 15*mm, 1.5*mm, fill=1, stroke=1)
    c.setFillColor(ACCENT)

# Bottom tagline
c.setFillColor(GREY)
c.setFont('Helvetica', 7)
c.drawCentredString(W/2, 15*mm, 'DECĒIT × COSMICO · 10 MAGGIO 2026')

# Page border
c.setStrokeColor(HexColor('#e8e8e8'))
c.setLineWidth(0.5)
c.rect(4*mm, 4*mm, W - 8*mm, H - 8*mm, fill=0, stroke=1)

c.showPage()

# === PAGE 2: RETRO (instructions) ===

c.setFillColor(WHITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Top accent bar
c.setFillColor(DARK)
c.rect(0, H - 8*mm, W, 8*mm, fill=1, stroke=0)

c.setFillColor(WHITE)
c.setFont('Helvetica', 7)
c.drawString(10*mm, H - 5.5*mm, 'DECĒIT')
c.drawRightString(W - 10*mm, H - 5.5*mm, 'COSMICO')

# Instructions header
c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 14)
c.drawString(12*mm, H - 28*mm, 'COME FUNZIONA')

# Step 1
c.setFillColor(ACCENT)
c.setFont('Helvetica-Bold', 10)
c.drawString(12*mm, H - 45*mm, '1.')
c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 9)
c.drawString(22*mm, H - 45*mm, 'Prendi una T-shirt di carta')
c.setFont('Helvetica', 8.5)
c.setFillColor(HexColor('#555555'))
c.drawString(12*mm, H - 52*mm, 'Scegline una dai tavoli — è la tua tela bianca.')

# Step 2
c.setFillColor(ACCENT)
c.setFont('Helvetica-Bold', 10)
c.drawString(12*mm, H - 67*mm, '2.')
c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 9)
c.drawString(22*mm, H - 67*mm, 'Disegna quello che vuoi')
c.setFont('Helvetica', 8.5)
c.setFillColor(HexColor('#555555'))
c.drawString(12*mm, H - 74*mm, 'Sul davanti: logo DECĒIT, scarabocchi, astratto —')
c.drawString(12*mm, H - 80*mm, 'libero sfogo. Sul retro: lascia nome ed email.')

# Step 3
c.setFillColor(ACCENT)
c.setFont('Helvetica-Bold', 10)
c.drawString(12*mm, H - 95*mm, '3.')
c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 9)
c.drawString(22*mm, H - 95*mm, 'Appendila al filo')
c.setFont('Helvetica', 8.5)
c.setFillColor(HexColor('#555555'))
c.drawString(12*mm, H - 102*mm, 'Le T-shirt resteranno in mostra per tutta la mattina.')

# Divider
c.setStrokeColor(HexColor('#e0e0e0'))
c.setLineWidth(0.5)
c.line(12*mm, H - 115*mm, W - 12*mm, H - 115*mm)

# Reward section
c.setFillColor(ACCENT)
c.setFont('Helvetica-Bold', 10)
c.drawString(12*mm, H - 130*mm, 'IL PREMIO')

c.setFont('Helvetica', 8.5)
c.setFillColor(DARK)
c.drawString(12*mm, H - 142*mm, 'Consegnando la tua T-shirt con i tuoi contatti,')
c.drawString(12*mm, H - 148*mm, 'ricevi una Tee DECĒIT × COSMICO da ritirare')
c.drawString(12*mm, H - 154*mm, 'gratuitamente presso DECĒIT Store in')
c.drawString(12*mm, H - 160*mm, 'via Abbrescia, 42 — Bari.')
c.drawString(12*mm, H - 168*mm, 'Ti invieremo via mail la comunicazione')
c.drawString(12*mm, H - 174*mm, 'per il ritiro.')

# Note
c.setFillColor(GREY)
c.setFont('Helvetica-Oblique', 7.5)
c.drawString(12*mm, H - 178*mm, 'Non vuoi lasciare i contatti? Nessun problema —')

c.drawString(12*mm, H - 184*mm, 'tieni la T-shirt disegnata come ricordo.')

# Bottom info
c.setFillColor(GREY)
c.setFont('Helvetica', 7)
c.drawCentredString(W/2, 15*mm, 'DECĒIT × COSMICO · 10 MAGGIO 2026')

# Page border
c.setStrokeColor(HexColor('#e8e8e8'))
c.setLineWidth(0.5)
c.rect(4*mm, 4*mm, W - 8*mm, H - 8*mm, fill=0, stroke=1)

c.save()
print('PDF creato: istruzioni-fustelle-A5.pdf')
