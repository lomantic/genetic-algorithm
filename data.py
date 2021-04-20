distance_A = {
    "B" : 10,
    "C" : 20,
    "D" : 30,
    "E" : 40,
    "F" : 50,
    "G" : 60,
    "H" : 20,
    "I" : 33,
    "J" : 62,
    "K" : 22
}

distance_B = {
    "A" : 10,
    "C" : 15,
    "D" : 25,
    "E" : 35,
    "F" : 45,
    "G" : 55,
    "H" : 65,
    "I" : 44,
    "J" : 33,
    "K" : 29
}
distance_C = {
    "A" : 20,
    "B" : 15,
    "D" : 35,
    "E" : 45,
    "F" : 55,
    "G" : 65,
    "H" : 44,
    "I" : 44,
    "J" : 10,
    "K" : 72
}
distance_D = {
    "A" : 30,
    "B" : 25,
    "C" : 35,
    "E" : 55,
    "F" : 20,
    "G" : 30,
    "H" : 72,
    "I" : 72,
    "J" : 20,
    "K" : 19
}

distance_E = {
    "A" : 40,
    "B" : 35,
    "C" : 45,
    "D" : 55,
    "F" : 10,
    "G" : 20,
    "H" : 11,
    "I" : 12,
    "J" : 38,
    "K" : 61
}
distance_F = {
    "A" : 50,
    "B" : 45,
    "C" : 55,
    "D" : 20,
    "E" : 10,
    "G" : 55,
    "H" : 24,
    "I" : 51,
    "J" : 41,
    "K" : 11

}
distance_G = {
    "A" : 60,
    "B" : 55,
    "C" : 65,
    "D" : 30,
    "E" : 20,
    "F" : 55,
    "H" : 10,
    "I" : 22,
    "J" : 60,
    "K" : 39

}
distance_H = {
    "A" : 20,
    "B" : 65,
    "C" : 44,
    "D" : 72,
    "E" : 11,
    "F" : 24,
    "G" : 10,
    "I" : 21,
    "J" : 58,
    "K" : 30

}
distance_I = {
    "A" : 33,
    "B" : 44,
    "C" : 44,
    "D" : 72,
    "E" : 12,
    "F" : 51,
    "G" : 22,
    "H" : 21,
    "J" : 57,
    "K" : 45

}
distance_J = {
    "A" : 62,
    "B" : 33,
    "C" : 10,
    "D" : 20,
    "E" : 38,
    "F" : 41,
    "G" : 60,
    "H" : 58,
    "I" : 57,
    "K" : 45

}
distance_K = {
    "A" : 22,
    "B" : 29,
    "C" : 72,
    "D" : 19,
    "E" : 61,
    "F" : 11,
    "G" : 39,
    "H" : 30,
    "I" : 45,
    "J" : 45

}

class Route:
    def __init__(self,order,length,fitness):
        self.order = order
        self.length =length
        self.fitness = fitness
    def testPrint(self):
        print("order : "+str(self.order))
        print("length : "+str(self.length))
        print("fitness : "+str(self.fitness))
