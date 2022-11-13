import requests

class extractor:
    def __init__(self, URL, token, path) -> None:
        self.URL = URL.split('/')[4]
        self.token = token
        self.path = path

        self.get_json()
        self.get_background()
        self.get_btns()
        self.get_images()
        self.get_entrys()

    def get_json(self):
        try:
            self.my_elements = requests.get(
                f'https://api.figma.com/v1/files/{self.URL}',
                headers={"X-FIGMA-TOKEN": self.token}
            )

            self.data = self.my_elements.json()
            self.window = self.data["document"]["children"][0]["children"][0]
            self.window_elements = self.window["children"]
        except ValueError:
            print("Value Error, Invalid Input. Please check your input and try again.")

        except requests.ConnectionError:
            print("No connection, The Project generator requires internet access to work.")

    def get_background(self):
        
        self.window_width, self.window_height = int(self.window["absoluteBoundingBox"]["width"]), int(self.window["absoluteBoundingBox"]["height"])

        for element in self.window_elements:
            if element['name'] == 'background' or element['name'] == 'Background':
                self.background = element

        back = requests.get(
                    f'https://api.figma.com/v1/images/{self.URL}?ids={self.background["id"]}',
                    headers={"X-FIGMA-TOKEN": f"{self.token}"}
                )

        back = requests.get(back.json()["images"][self.background['id']])

        with open(f"{self.path}/resources/{self.background['name']}.png", "wb") as file:
                file.write(back.content)
        file.close()
    
    def get_btns(self):
        self.btns = []

        for element in self.window_elements:
            if 'btn' in element['name']:
                self.btns.append(element)

    def get_entrys(self):
        self.entrys = []

        for element in self.window_elements:
            if 'entry' in element['name']:
                self.entrys.append(element)

    def get_images(self):
        responces = []

        for item in self.btns:
            responces.append(
                requests.get(
                    f'https://api.figma.com/v1/images/{self.URL}?ids={item["id"]}',
                    headers={"X-FIGMA-TOKEN": f"{self.token}"}
                )
            )

        self.img_btns = []

        for response, btn in zip(responces, self.btns):
            self.img_btns.append((requests.get(response.json()["images"][btn['id']]), btn['name']))

        print('generardo botones')
        print(self.path)
        for img in self.img_btns:
            #(f"{self.path}/resources/{img[1]}.png", "wb")
            with open(f"{self.path}/resources/{img[1]}.png", "wb") as file:
                file.write(img[0].content)
            file.close()
                    
    def get_data(self):

        return self.btns, self.entrys
