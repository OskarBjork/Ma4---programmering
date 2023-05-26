import math

reZ = float(input("Re: "))
imZ = float(input("Im: "))

absZ = math.sqrt(reZ**2 + imZ**2)

if reZ > 0 and imZ > 0:
    argZ = math.atan(imZ / reZ)
elif reZ < 0 and imZ > 0:
    print("2. kvadrant")
    argZ = math.pi - math.atan(imZ / abs(reZ))
elif reZ < 0 and imZ < 0:
    print("3. kvadrant")
    argZ = math.pi + math.atan(imZ / reZ)
elif reZ > 0 and imZ < 0:
    print("4. kvadrat")
    argZ = 2 * math.pi - math.atan(abs(imZ) / reZ)

argZ = round(argZ, 3)
absZ = round(absZ, 3)

print(f"Polär form: {absZ}*(cos({argZ}) + isin({argZ}))")
