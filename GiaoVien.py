from Nguoi import Nguoi


class GiaoVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_gv, so_nam_kn, chuyen_mon, luong):
        super().__init__(ten, gioi_tinh, tuoi, dia_chi)
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
    
    def __repr__(self):
        return '{' + self.getMaGV() + ', ' + self.getTen() + ', ' + str(self.getTuoi()) + ', ' + str(self.getSoNamKN()) + '}'

    @classmethod
    def nhap(cls):
        nguoi = Nguoi.nhap()
        ma_gv = input("Nhap ma giao vien: ")
        so_nam_kn = input("Nhap so nam kinh nghiem: ")
        chuyen_mon = input("Nhap chuyen mon: ")
        luong = input("Nhap luong: ")
        return GiaoVien(nguoi.getTen(), nguoi.getGioiTinh(), nguoi.getTuoi(), nguoi.getDiaChi(),
                    ma_gv, so_nam_kn, chuyen_mon, luong)

if __name__ == "__main__":
    print("_____Nhap giao vien______")
    gv1 = GiaoVien.nhap()
    print("_____Nhap giao vien")
    gv2 = GiaoVien.nhap()
    print("_____Nhap giao vien______")
    gv3 = GiaoVien.nhap()

    ds_gv = [gv1, gv2, gv3]
    # 1. Sap xep theo ma giao vien tang dan
    ds_gv.sort(key=lambda x: x.getMaGV())
    print(ds_gv)

    # 2. Sap xep theo so nam kinh nghiem giam dan
    ds_gv.sort(key=lambda x: float(x.getSoNamKN()), reverse=True)
    print(ds_gv)