import math
magnolii = int(input())
zumbul = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

collected = magnolii * 3.25 + zumbul * 4 + roses * 3.50 + cactus * 8
collected = collected - 0.05 * collected
if collected >= gift_price:
    print(f"She is left with {math.floor(collected - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - collected)} leva.")
