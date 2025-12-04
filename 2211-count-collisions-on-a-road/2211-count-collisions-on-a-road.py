class Solution:
    def countCollisions(self, direc: str) -> int:
        direc=direc.lstrip("L")
        direc=direc.rstrip("R")
        return direc.count("R")+direc.count("L")