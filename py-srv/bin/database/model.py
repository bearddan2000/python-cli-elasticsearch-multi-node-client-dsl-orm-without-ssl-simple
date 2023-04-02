from elasticsearch_dsl import Document,Text,Keyword,Long,Double,Integer

class DbModel(Document):
    id=Long()
    name=Text()
    breed=Text()
    color=Keyword()
    height=Double()
    age=Integer()

    class Index:
        name='dog-demo' #index will be created automatically

    def __init__(self, id, name, breed, color: str, height, age) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.breed = breed
        self.color = color.split('::')
        self.height = height
        self.age = age
