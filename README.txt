a modified json because i got bored
WOW IT FINALLY WORKS YAYAYYAYAYYAYYAYYAYYA IM SO HAPPY RIGHT NOW

>>> import antigrav
>>> from cmath import sqrt
>>> antigrav.dump({"int": 2234, "float": 324.235, "str": "qoofy string", "list": [1, 2, "hello moon", [3, 4, [[5]]]], "tuple": ("amigger", "and", "his", "family"), "dict": {1: 2, 3: 4, 5: {6: 7}}, "complex": sqrt(-1)}, open("test.antigrav", "w"), sort_keys=True, indent=4)
>>> open("test.antigrav").read()
{
    "complex": 0.0+1.0i, # <- complex numbers do work
    "dict": {
        "1": 2,
        "3": 4,
        "5": {
            "6": 7
        }
    },
    "float": 324.235,
    "int": 2234,
    "list": [
        1,
        2,
        "hello moon",
        [
            3,
            4,
            [
                [
                    5
                ]
            ]
        ]
    ],
    "str": "qoofy string",
    "tuple": [
        "amigger",
        "and",
        "his",
        "family"
    ]
}