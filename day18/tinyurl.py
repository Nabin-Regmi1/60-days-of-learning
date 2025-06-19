class Codec:
    ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.id = 1
        self.code2url = {}
        self.url2code = {}

    def _to_base62(self, n):
        if n == 0:
            return self.ALPHABET[0]
        s = []
        while n:
            n, r = divmod(n, 62)
            s.append(self.ALPHABET[r])
        return ''.join(reversed(s))

    def encode(self, longUrl):
        if longUrl in self.url2code:
            code = self.url2code[longUrl]
        else:
            code = self._to_base62(self.id)
            self.id += 1
            self.url2code[longUrl] = code
            self.code2url[code] = longUrl
        return "https://tinyurl.com/" + code

    def decode(self, shortUrl):
        code = shortUrl.rsplit('/', 1)[-1]
        return self.code2url.get(code, "")

hello=Codec()
hello1=hello.encode("https://leetcode.com/problems/design-tinyurl")
print(hello1)
hello2=hello.decode(hello1)
print(hello2)
