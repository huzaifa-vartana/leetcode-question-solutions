class RandomNumberGenerator:
    @staticmethod
    def generate_random_string(length = 7):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

class Codec:
    PREFIX = "tinyurl"
    def __init__(self) -> None:
        # generate a random number for the short url and it should be unique
        self.hash = dict()


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        random_string = None
        while True:
            random_string = RandomNumberGenerator.generate_random_string()
            if random_string not in self.hash:
                break

        self.hash[random_string] = longUrl
        return "https://" + Codec.PREFIX + "/" + random_string

    def decode(self, shortUrl: str) -> str:
        longUrl = self.hash[shortUrl.split("/")[-1]]
        return longUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))