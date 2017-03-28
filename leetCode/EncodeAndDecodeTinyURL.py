import random
class Codec:
    def __init__(self):
        self.dic = {}

    def encode(self, longUrl):
        encoded = ""
        for key, url in self.dic.items():
            if url == longUrl:
                return key
        for i in range(6):
            c = random.randrange(0, 62)
            if c < 10:
                encoded += str(c)
            elif c < 36:
                encoded += chr(ord("a") + c - 10)
            else:
                encoded += chr(ord("A") + c - 36)
        self.dic[encoded] = longUrl
        return encoded

    def decode(self, shortUrl):
        return self.dic[shortUrl]


codec = Codec()
longURL = "https://www.yskang.com"
encodedURL = codec.encode(longURL)
print(encodedURL)
decodedURL = codec.decode(encodedURL)
print(decodedURL)
