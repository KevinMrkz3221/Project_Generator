import templates

class CBtn:
    def __init__(self, data) -> None:

        self.x = round(data['absoluteBoundingBox']['x'])
        self.y = round(data['absoluteBoundingBox']['y'])
        self.path = f'./resources/{data["name"]}.png'
        self.name = data['name']

    def generate_btn(self):
        self.my_btn = templates.button_template.replace('my_name', self.name).replace('my_x', str(self.x)).replace('my_y', str(self.y)).replace('my_path', self.path)

        return self.my_btn

    def __str__(self) -> str:
        return f'{self.x}  | {self.y} | {self.path}'
