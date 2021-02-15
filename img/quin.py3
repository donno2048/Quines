from PIL import ImageDraw
i=ImageDraw.Image.new('L',(2000,40));r="from PIL import ImageDraw\ni=ImageDraw.Image.new('L',(2000,40));r=%r;ImageDraw.Draw(i).text((0,0),r%%r,fill=255);i.save('test.png')";ImageDraw.Draw(i).text((0,0),r%r,fill=255);i.save('test.png')
