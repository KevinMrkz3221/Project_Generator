import templates

class CEntry:
    def __init__(self, data) -> None:
        self.x = round(data['absoluteBoundingBox']['x'])
        self.y = round(data['absoluteBoundingBox']['y'])
        self.color = self.get_color(data)
        self.width = round(data['absoluteBoundingBox']['width'])
        self.height = round(data['absoluteBoundingBox']['height'])
        self.name = data['name']
        

    def get_color(self, data):
        r = data["fills"][0]["color"]["r"] * 255
        g = data["fills"][0]["color"]["g"] * 255
        b = data["fills"][0]["color"]["b"] * 255

        color = ('#%02x%02x%02x' % (round(r), round(g), round(b)))
        return color

    def generate_entry(self):
        self.my_entry = templates.entry_template.replace('my_name', self.name).replace('my_x', str(self.x)).replace('my_y', str(self.y)).replace('my_color', self.color).replace('my_width', str(self.width)).replace('my_height', str(self.height))
        return self.my_entry

    def __str__(self) -> str:
        return f'{self.x} | {self.y} | {self.color} | {self.width} | {self.height}'