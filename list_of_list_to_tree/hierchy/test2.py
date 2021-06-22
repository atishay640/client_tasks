from test_hierarchy import checkEqual


flat_hierarchy = [
    ['Europe', 'DE', 'Berlin', 'Wolfgang Muller'],
    ['Europe', 'DE', 'Berlin', 'Paul Geotze'],
    ['Europe', 'DE', 'Berlin', 'Julia Klopp'],
    ['Europe', 'DE', 'Karlsruhe', 'Jurgen Klopp'],
    ['Europe', 'DE', 'Karlsruhe', 'Felix Engel'],
    ['Europe', 'DE', 'Karlsruhe', 'Sebastian Walther'],
    ['Europe', 'UK', 'Borris Johnson'],
    ['Europe', 'UK', 'Harry Kane'],
    ['Africa', 'Sadio Mane'],
    ['Africa', 'Mo Salah'],
    ['North America', 'US', 'California', 'San Fransisco', 'Matt Smith'],
    ['North America', 'US', 'California', 'San Fransisco', 'Travis Noe'],
    ['North America', 'US', 'California', 'San Fransisco', 'Itan Chavira'],
    ['North America', 'US', 'California', 'San Fransisco', 'Travis Hawkins']
]


class Node:
    objects = set()

    @classmethod
    def all(Node):
        return Node.objects

    @classmethod
    def get(Node, value):
        for existing_node in Node.all():
            if existing_node.value == value:
                return existing_node
        return None

    def __init__(self, value, parent=None) -> None:
        if Node.get(value):
            return Node.get(value)

        if parent == None:
            self.parent = "ROOT"
        else:
            self.parent = parent
            
        self.value = value
        self.children = set()
        self.objects.add(self)
    
    def add_child(self, node):
        node.parent = self.value
        self.children.add(node)
        return node

    def get_children(self):
        return self.children if self.children else None

    def get_parent(self):
        return self.parent.value if self.parent and  self.parent != "ROOT" and self.parent.value else None

    def __repr__(self) -> str:
        return f"< Tree{self.value} > "


def add_data():
    root = Node("flat_hierarchy")
    parent = root
    for data_list in flat_hierarchy:
        for value in data_list:
            node= Node.get(value)
            if node:
                node = parent.add_child(node)
            else:
                node = parent.add_child(Node(value))
            parent = node
        parent = root

add_data()
root = Node.get("flat_hierarchy")

def fetch_data_dict(node: Node):
    dd = {}
    if node.get_children():
        for n1 in node.get_children():
            dd[n1.value] = list(n1.get_children())
            for n2 in n1.get_children():
                dd[n2.value] = n2.get_children()
                if n2 and n2.get_children():
                    for n3 in n2.get_children():
                        dd[n3.value] = n3.get_children()
            
        print(dd)

            

    return None
    

fetch_data_dict(root)

hierarchy = {
    'Europe': {
        'DE': {
            'Berlin': ['Wolfgang Muller', 'Paul Geotze', 'Julia Klopp'],
            'Karlsruhe': ['Jurgen Klopp', 'Felix Engel', 'Sebastian Walther'],
        },
        'UK': ['Borris Johnson', 'Harry Kane'],
    },
    'Africa': ['Sadio Mane', 'Mo Salah'],
    'North America': {
        'US': {
            'California': {
                'San Fransisco': ['Matt Smith', 'Travis Noe', 'Itan Chavira', 'Travis Hawkins'],
            }
        }
    }
}
