class MonHoc:
    def __init__(self, ma, ten, so_tin_chi):
        self._ma = ma
        self._ten = ten
        self._so_tin_chi = so_tin_chi

    def getMa(self):
        return self._ma

    def getTen(self):
        return self._ten

    def getSoTinChi(self):
        return self._so_tin_chi

    @classmethod
    def nhap(cls):
        ma = input("Nhap ma mon hoc: ")
        ten = input("Nhap ten mon hoc: ")
        so_tin_chi = input("Nhap so tin chi: ")
        return MonHoc(ma, ten, so_tin_chi)