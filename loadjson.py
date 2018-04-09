import json


class LoadJsonFile:
      def __init__(self, filename):

        with open(filename, encoding="utf-8-sig") as f:
            data = json.load(f)
            item = data["postgres"]

            self.host = item["host"]
            self.database = item["database"]
            self.user = item["user"]
            self.password = item["password"]
            f.close()

if __name__ == "__main__":
    file = LoadJsonFile("./database/config.json")
    print(file.host)

