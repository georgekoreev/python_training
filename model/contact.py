from sys import maxsize


class Contact:

    def __init__(self, name=None, sname=None, address=None, id=None):
        self.name = name
        self.sname = sname
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.sname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.sname == other.sname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize