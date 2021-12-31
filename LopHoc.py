from GiaoVien import GiaoVien
from SinhVien import SinhVien
from MonHoc import MonHoc

class LopHoc:
    def __init__(self, ma, ten, so_sv, giao_vien, ds_sv, mon_hoc):
        self._ma = ma
        self._ten = ten
        self._so_sv = so_sv
        self._giao_vien = giao_vien
        self._ds_dv = ds_sv
        self._mon_hoc = mon_hoc

    def getMa(self):
        return self._ma

    def getTen(self):
        return self._ten

    def getSoSV(self):
        return self.so_sv

    @classmethod
    def nhap(cls):
        ma = input("Nhap ma lop hoc: ")
        ten = input("Nhap ten lop hoc: ")
        so_sv = input("Nhap so sinh vien: ")
        print("NHAP THONG TIN GIAO VIEN")
        giao_vien = GiaoVien.nhap()
        print("NHAP DANH SACH SINH VIEN")
        ds_sv = []
        for i in range(int(so_sv)):
            sv = SinhVien.nhap()
            ds_sv.append(sv)
        print("NHAP MON HOC")
        monhoc = MonHoc.nhap()
        return LopHoc(ma, ten, so_sv, giao_vien, ds_sv, monhoc)