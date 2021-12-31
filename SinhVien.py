from Nguoi import Nguoi


class SinhVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_sv, lop, chuyen_nganh):
        super().__init__(ten, gioi_tinh, tuoi, dia_chi)
        self._ma_sv = ma_sv
        self._lop = lop
        self._chuyen_nganh = chuyen_nganh

    def getMaSV(self):
        return self._ma_sv

    def getLop(self):
        return self._lop

    def getChuyenNganh(self):
        return self._chuyen_nganh
    
    @classmethod
    def nhap(cls):
        nguoi = Nguoi.nhap()
        ma_sv = input("Nhap ma sinh vien: ")
        lop = input("Nhap lop: ")
        chuyen_nganh = input("Nhap chuyen nganh: ")
        print("_________________________")

        return SinhVien(nguoi.getTen(), nguoi.getGioiTinh(), nguoi.getTuoi(), nguoi.getDiaChi(),
                    ma_sv, lop, chuyen_nganh)
    
    def __repr__(self):
        return '{' + self.getMaSV() + ', ' + self.getTen() + ', ' + str(self.getGioiTinh()) + ', ' + str(self.getTuoi()) + '}'

if __name__ == "__main__":
    ds_sinh_vien = [
        SinhVien.nhap(),
        SinhVien.nhap()
    ]
    # 1. Sap xep theo ten tang dan
    ds_sinh_vien.sort(key=lambda x: x.getTen())
    print(ds_sinh_vien)

    # 2. Sap xep theo ten, theo sau la den tuoi giam dan
    ds_sinh_vien.sort(key=lambda x: (x.getTen(), int(x.getTuoi())), reverse=True)
    print(ds_sinh_vien)