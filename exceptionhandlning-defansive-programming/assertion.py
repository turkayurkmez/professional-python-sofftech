def getSquare(x):
    assert isinstance(x, (int,float)), f"x parametresi sayısal bir tip olmalı. Şu anda {type(x)}"
    assert x>=0, f"x değeri negatif olamaz. Şu anki değer: {x}"

    return x**2

try:
    getSquare(4)
    getSquare(2.5)
    #getSquare("hadi")
    #getSquare(-5)
except AssertionError as custom:
    print(custom)
