
import sys             #a python module with system functions for this OS
import py2neo
import datetime
from py2neo import Graph, Path, Relationship , Node


tagsList = []

class Tag:
    def __init__(self, userId, movieId,tag):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag


def initTags():
    print("start Tags Load" + str(datetime.datetime.now()))
    with open('tags.dat') as inf:
        for line in inf:
            line = line.strip()
            userID, movieID, tag, timeStamp = line.split("::")  # split line at blanks (by default),
            tagNew = Tag(userID,movieID,tag)
            tagsList.append(tagNew)
    inf.close()
    print("Ended Tags Load" + str(datetime.datetime.now()))
    return
    
    


##################BEGIN PROCESS HERE#########################
# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------
initTags()
graph = Graph()


graph.delete_all()


#CREATE ALL GENRE NODES HERE
ActionGenreNode = Node("Genre", name="Action")
AdventureGenreNode = Node("Genre", name="Adventure")
AnimationGenreNode = Node("Genre", name="Animation")
ChildrensGenreNode = Node("Genre", name="Childrens")
ComedyGenreNode = Node("Genre", name="Comedy")
CrimeGenreNode = Node("Genre", name="Crime")
DocumentaryGenreNode = Node("Genre", name="Documentary")
DramaGenreNode = Node("Genre", name="Drama")
FantasyGenreNode = Node("Genre", name="Fantasy")
FilmNoirGenreNode = Node("Genre", name="FilmNoir")
HorrorGenreNode = Node("Genre", name="Horror")
MusicalGenreNode = Node("Genre", name="Musical")
MysteryGenreNode = Node("Genre", name="Mystery")
RomanceGenreNode = Node("Genre", name="Romance")
SciFiGenreNode = Node("Genre", name="SciFi")
ThrillerGenreNode = Node("Genre", name="Thriller")
WarGenreNode = Node("Genre", name="War")
WesternGenreNode = Node("Genre", name="Western")



for line in sys.stdin:
    print(line)
#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
# movie file format -->MovieID::Title::Genres
#1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy
    
    line = line.strip()  #strip is a method, ie function, associated
                         #  with string variable, it will strip 
                         #   the carriage return (by default)
                         
    movieID,title,genres = line.split("::")  #split line at blanks (by default)
    genreList = genres.split("|")
    #print(movieID)
    #print(title)
    newTitle = title.replace("'","")
   

       # movieInsert = "CREATE (Movie" + str(movieID) + ":Movie {title:'" + str(newTitle) + "',movieId:" + str(movieID) + ",name:'Movie"+str(movieID)+"'})"
    #create the Movie Node here
    movieNode = Node("Movie", name="Movie"+str(movieID),title=str(newTitle))
    for tempGenre in genreList:
        tempGenre = tempGenre.replace("-","").replace("'","")

        #Create realtionship between movie and genre here
        if str(tempGenre) =='Action':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", ActionGenreNode))
        if str(tempGenre) ==  'Adventure':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", AdventureGenreNode))
        if str(tempGenre) =='Animation':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", AnimationGenreNode))
        if str(tempGenre) ==  'Childrens':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", ChildrensGenreNode))
        if str(tempGenre) ==  'Comedy':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", ComedyGenreNode))
        if str(tempGenre) ==  'Crime':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", CrimeGenreNode))
        if str(tempGenre) == 'Documentary':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", DocumentaryGenreNode))
        if str(tempGenre) ==  'Drama':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", DramaGenreNode))
        if str(tempGenre) == 'Fantasy':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", FantasyGenreNode))
        if str(tempGenre) ==  'FilmNoir':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", FilmNoirGenreNode))
        if str(tempGenre) ==  'Horror':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", HorrorGenreNode))
        if str(tempGenre) ==   'Musical':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", MusicalGenreNode))
        if str(tempGenre) ==   'Mystery':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", MysteryGenreNode))
        if str(tempGenre) ==   'Romance':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", RomanceGenreNode))
        if str(tempGenre) ==   'SciFi':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", SciFiGenreNode))
        if str(tempGenre) ==   'Thriller':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", ThrillerGenreNode))
        if str(tempGenre) ==   'War':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", WarGenreNode))
        if str(tempGenre) ==   'Western':
            graph.create(Relationship(movieNode, "IS_CLASSIFIED_AS", WesternGenreNode))


	##Create Tags Relationship here
    print("movieNode TITLE====------------------"+title+"---------------------->"+str(movieNode))
    newTagsList = filter(lambda x: x.movieId == movieID, tagsList)

    print("number of tags for movieId=>" + movieID + "----count is==>" + str(len(newTagsList)))
    
    tempUserID = ""
    for tempTag in newTagsList:
        taggerNode = Node("Tag",tag=str(tempTag.tag),userid=str(tempTag.userId))
        print("tagNode Tag====>" + str(taggerNode))
        graph.create(Relationship(taggerNode, "TAGGED",movieNode ))


