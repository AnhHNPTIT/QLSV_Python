class LopHoc:
    def __init__(self, ma, ten, so_sv, giao_vien, ds_sv):
        self._ma = ma
        self._ten = ten
        self._so_sv = so_sv
        self._giao_vien = giao_vien
        self._ds_dv = ds_sv

    def getMa(self):
        return self._ma

    def getTen(self):
        return self._ten

    def getSoSV(self):
        return self.so_sv
