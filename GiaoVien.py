from Nguoi import Nguoi


class GiaoVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_gv, so_nam_kn, chuyen_mon, luong):
        super.__init__(self, ten, gioi_tinh, tuoi, dia_chi)
        self._ma_gv = ma_gv
        self._so_nam_kn = so_nam_kn
        self._chuyen_mon = chuyen_mon
        self._luong = luong

    def getMaGV(self):
        return self._ma_gv

    def getSoNamKN(self):
        return self._so_nam_kn

    def getChuyenMon(self):
        return self._chuyen_mon

    def getLuong(self):
        return self._luong