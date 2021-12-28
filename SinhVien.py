from Nguoi import Nguoi


class SinhVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_sv, lop, chuyen_nganh):
        super.__init__(self, ten, gioi_tinh, tuoi, dia_chi)
        self._ma_sv = ma_sv
        self._lop = lop
        self._chuyen_nganh = chuyen_nganh

    def getMaSV(self):
        return self._ma_sv

    def getLop(self):
        return self._lop

    def getChuyenNganh(self):
        return self._chuyen_nganh