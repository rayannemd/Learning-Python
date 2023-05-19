lengthal = float(input("Enter the length of the rectangle: "))
numberolal = float(input("How many sides measure this size? "))
widthal = float(input("Enter the width of the rectangle: "))
numberowal = float(input("How many sides measure this size? "))
height = float(input("Enter the height of the rectangle: "))

al = numberolal * lengthal * height + numberowal * widthal * height
ab = lengthal * widthal

area = 2 * ab + al
volume = ab * height

print(f"The area of the prism is: {area}cm2 and the volume is: {volume}cm3")
