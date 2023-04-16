
from PIL import Image, ImageDraw
import cairo

def generate_image():
    #return "Hello"
 
    #img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    # 
    #d1 = ImageDraw.Draw(img)
    #d1.text((10,10), "Hello World", fill=(255,255,0))
    
    im = Image.new('RGB', (500, 300), (128, 128, 128))
    draw = ImageDraw.Draw(im)
    draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
    draw.line((100, 200, 450, 100), fill=(255, 255, 0), width=1)
    draw.line((200, 200, 450, 100), fill=(255, 255, 0), width=1)
    im.save('my_image.png')

    #with cairo.SVGSurface("example.svg", 200, 200) as surface:
    #    context = cairo.Context(surface)
    #    x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
    #    x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
    #    context.scale(200, 200)
    #    context.set_line_width(0.04)
    #    context.move_to(x, y)
    #    context.curve_to(x1, y1, x2, y2, x3, y3)
    #    context.stroke()
    #    context.set_source_rgba(1, 0.2, 0.2, 0.6)
    #    context.set_line_width(0.02)
    #    context.move_to(x, y)
    #    context.line_to(x1, y1)
    #    context.move_to(x2, y2)
    #    context.line_to(x3, y3)
    #    context.stroke()
    #    surface.write_to_png("my_other_image.png")

    with cairo.SVGSurface("example.svg", 200, 200) as surface:
        context = cairo.Context(surface)
        x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
        x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
        context.scale(200, 200)
        # curvy bit
        context.set_line_width(0.04)
        context.move_to(x, y)
        context.curve_to(x1, y1, x2, y2, x3, y3)
        context.stroke()
        # straight lines
        context.set_source_rgba(1, 0.2, 0.2, 0.6)
        context.set_line_width(0.02)
        context.move_to(x, y)
        # line1
        context.line_to(x1, y1)
        context.move_to(x2, y2)
        # line2
        context.line_to(x3, y3)
        context.stroke()
        surface.write_to_png("my_other_image.png")

    from math import pi
    from cairo import SVGSurface, Context, Matrix

    #WIDTH = 6 * 72
    #HEIGHT = 4 * 72
    WIDTH = 6 * 100
    HEIGHT = 4 * 100

    s = SVGSurface('example1.svg', WIDTH, HEIGHT)
    c = Context(s)

    # Transform to normal cartesian coordinate system
    m = Matrix(yy=-1, y0=HEIGHT)
    c.transform(m)

    # Set a background color
    c.save()
    c.set_source_rgb(0.3, 0.3, 1.0)
    c.paint()
    c.restore()

    c.move_to(0, 0)
    i = 1
    #while i < 10:
    #    c.line_to(2 + i * 72,i * 72)
    #    i += 1
    a, b = 2, 1
    while b < 10:
        a, b = b, a+b
        c.line_to(a * 20, b * 20)
    #c.line_to(3 * 72,4 * 72)
    c.close_path()
    c.save()
    c.set_line_width(6.0)
    c.stroke_preserve()
    c.set_source_rgb(0.3, 0.8, 0.9)
    c.fill()
    c.restore()

    # Draw some lines
    c.move_to(0, 0)
    c.line_to(2 * 72, 2 * 72)
    c.line_to(3 * 72, 1 * 72)
    c.line_to(4 * 72, 2 * 72)
    c.line_to(6 * 72, 0)
    c.close_path()
    c.save()
    c.set_line_width(6.0)
    c.stroke_preserve()
    c.set_source_rgb(0.3, 0.3, 0.3)
    c.fill()
    c.restore()

    # Draw a circle
    c.save()
    c.set_line_width(6.0)
    c.arc(1 * 72, 3 * 72, 0.5 * 72, 0, 2 * pi)
    c.stroke_preserve()
    c.set_source_rgb(1.0, 1.0, 0)
    c.fill()
    c.restore()

    # Save as a SVG and PNG
    s.write_to_png('example1.png')
    s.finish()

# https://en.wikipedia.org/wiki/Cartesian_tree