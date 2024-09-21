import random


class Codec:

    def __init__(self) -> None:
        # generate a random number for the short url and it should be unique
        self.map = dict()

    def generate_short_url(self, longUrl: str) -> str:
        scheme, *rem_url = longUrl.split("//")
        domain, *parts = rem_url[0].split("/")

        short_url = ""

        if domain not in self.map:

            short_domain = ""
            for i in range(6):
                short_domain += chr(random.randint(97, 122))
            self.map[domain] = short_domain

        short_url += self.map[domain]

        for part in parts:
            short_part = ""
            if part in self.map:
                short_part = self.map[part]
            else:
                for i in range(6):
                    short_part += chr(random.randint(97, 122))
                self.map[part] = short_part

            short_url += "/" + short_part

        return short_url

    def encode(self, longUrl: str) -> str:

        encoded_url = ""

        short_url = self.generate_short_url(longUrl)
        self.map[short_url] = longUrl
        encoded_url = f"http://tinyurl.com/{short_url}"

        print(encoded_url)
        return encoded_url

    def decode(self, shortUrl: str) -> str:
        short_url = shortUrl.split("http://tinyurl.com/")[1]
        long_url = self.map[short_url]
        print(long_url)
        return long_url
