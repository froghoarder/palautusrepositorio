from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        content_de = toml.loads(content)
        
        return Project(content_de["tool"]["poetry"]["name"], content_de["tool"]["poetry"]["description"], content_de["tool"]["poetry"]["license"], \
        content_de["tool"]["poetry"]["authors"], content_de["tool"]["poetry"]["dependencies"], content_de["tool"]["poetry"]["group"]["dev"]["dependencies"])
