import os
from database.model import DbModel
from database.schema import COLUMN_NAME

INDEX_NAME = os.environ["INDEX_NAME"]

DOC = [
    DbModel(0,"Bruno","Pincher","black::brown",5.2,1),
    DbModel(1,"Bull","Pitbull","white::brown",4.9,10),
    DbModel(2,"Tiny","Teacup","white",1.6,15),
    DbModel(3,"Bruno","WolfHound","grey",5.1,5),
    DbModel(4,"Fred","Newfoundland","yellow::black",5.4,7),
    DbModel(5,"Ruffus","Snozier","black::white::brown",3.6,2),
    DbModel(6,"Dog","Shepard","brown::yellow::black",4.9,12),
    DbModel(7,"Max","Mastif","spotted::brown",7.8,6),
    DbModel(8,"Billi","Am.Bulldog","white::grey",4.3,4),

]