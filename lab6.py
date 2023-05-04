import math
from decimal import Decimal

radius = float(input('Введіть радіус кулі >>> '))
PI = math.pi
volume = 4 / 3 * PI * radius ** 3
right_volume = Decimal(str(volume)).quantize(Decimal('0.01'))
print(right_volume)
