class Solution:
    def countValidWords(self, sentence):
        res = 0
        tokens = sentence.split(" ")
        
        for token in tokens:
            if token.lower() != token:
                continue
            if token.index(".") and token.index(".") < len(token) - 1 or token.count(".") > 1:
                continue
            if token.count("-") > 1 or token[-1] == "-" or token[0] == "-":
                continue
            res += 1
        return res

