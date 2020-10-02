def get_indices_of_item_weights(weights, length, limit):

    cache = {}
    for i in range(length-1):
        for x in range(len(weights[i:])):
            print(x)
            # #x+1
            # #if i != x+1:
            # print(weights[i], weights[i+x+1])
            # #if cache[weights[i] + ]

    return None

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))
# self.assertTrue(answer_4[0] == 6)
# self.assertTrue(answer_4[1] == 2)