
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import os

participants = []

with open("input.csv","rb") as f:
	reader = csv.reader(f)
	participants.extend(row[0] for row in reader)
fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
font = ImageFont.truetype(os.path.join(fonts_path, 'best_font.ttf'), 80)

output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Output')



for i, name in enumerate(participants, start=1):

	img = Image.open("sample_in.jpg")
	draw = ImageDraw.Draw(img)
	fsize_x , fsize_y = draw.textsize(name,font)

	x = 1065-(fsize_x)/2
	y = 510-(fsize_y)/2
	draw.text( (x , y) ,name,(0,0,0),font)

	output_name = os.path.join(output_path, f"{str(i)} - {name}.jpg")
	img.save(output_name)