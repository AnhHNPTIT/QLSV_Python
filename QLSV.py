from BangDiem import BangDiem
from GiaoVien import GiaoVien
from LopHoc import LopHoc
from MonHoc import MonHoc
from Nguoi import Nguoi
from SinhVien import SinhVien


class QLSV:
    ds_sv = []
    ds_gv = []
    ds_mon = []
    ds_lop = []
    bang_diem = []

    def tim_sv(self, ma_sv):
        result = None
        if (self.ds_sv.__len__() > 0):
            for sv in self.ds_sv:
                if (sv.getMaSV() == ma_sv):
                    result = sv
        return result

    def nhap_sv(self):
        nguoi = Nguoi.nhap()
        ma_sv = input("Nhap ma sinh vien: ")
        lop = input("Nhap lop: ")
        chuyen_nganh = input("Nhap chuyen nganh: ")
        return SinhVien(nguoi.getTen(), nguoi.getGioiTinh(), nguoi.getTuoi(), nguoi.getDiaChi(),
                    ma_sv, lop, chuyen_nganh)
    
    def them_sv(self):
        sinh_vien = self.nhap_sv()
        self.ds_sv.append(sinh_vien)

    def them_gv(self):
        nguoi = Nguoi.nhap()
        ma_gv = input("Nhap ma giao vien: ")
        so_nam_kn = input("Nhap so nam kinh nghiem: ")
        chuyen_mon = input("Nhap chuyen mon: ")
        luong = input("Nhap luong: ")
        giao_vien = GiaoVien(nguoi.getTen(), nguoi.getGioiTinh(), nguoi.getTuoi(), nguoi.getDiaChi(),
                    ma_gv, so_nam_kn, chuyen_mon, luong)
        self.ds_gv.append(giao_vien)

    def tim_mon(self, ma_mon):
        result = None
        if (self.ds_mon.__len__() > 0):
            for mon in self.ds_mon:
                if (mon.get_ma() == ma_mon):
                    result = mon
        return result

    def them_mon(self):
        ma = input("Nhap ma mon hoc: ")
        ten = input("Nhap ten mon hoc: ")
        so_tin_chi = input("Nhap so tin chi: ")
        mon_hoc = MonHoc(ma, ten, so_tin_chi)
        self.ds_mon.append(mon_hoc)

    def them_lop(self):
        ma = input("Nhap ma lop hoc: ")
        ten = input("Nhap ten lop hoc: ")
        so_sv = input("Nhap so sinh vien: ")
        print("Nhap thong tin giao vien")
        giao_vien = GiaoVien.nhap()
        print("Nhap danh sach sinh vien")
        ds_sv_lop = []
        for i in range(int(so_sv)):
            sv = self.nhap_sv()
            ds_sv_lop.append(sv)
        print("NHAP MON HOC")
        mon_hoc = MonHoc.nhap()
        lop_hoc = LopHoc(ma, ten, so_sv, giao_vien, ds_sv_lop, mon_hoc)
        self.ds_lop.append(lop_hoc)

    def them_diem(self):
        ma_sv = input("Nhap ma sinh vien: ")
        ma_mon_hoc = input("Nhap ma mon hoc: ")
        sinh_vien = self.tim_sv(ma_sv)
        mon_hoc = self.tim_mon(ma_mon_hoc)
        so_diem = input("Nhap so diem: ")
        diem = BangDiem(sinh_vien, mon_hoc, so_diem)
        self.bang_diem.append(diem)

    def sap_xep_tang(self):
        for i in range(self.bang_diem.__len__()):
            for j in range(i + 1, self.bang_diem.__len__()):
                if (self.bang_diem[i].get_sinh_vien().getTen() > self.bang_diem[j].get_sinh_vien().getTen()):
                    self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
                elif self.bang_diem[i]._sinh_vien.getTen() == self.bang_diem[j]._sinh_vien.getTen():
                    if self.bang_diem[i].get_so_diem() > self.bang_diem[j].get_so_diem():
                        self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
        for i in self.bang_diem:
            print(i)


    def sap_xep_giam(self):
        for i in range(self.bang_diem.__len__()):
            for j in range(i + 1, self.bang_diem.__len__()):
                if (self.bang_diem[i].get_sinh_vien().getTen() < self.bang_diem[j].get_sinh_vien().getTen()):
                    self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
                elif self.bang_diem[i]._sinh_vien.getTen() == self.bang_diem[j]._sinh_vien.getTen():
                    if self.bang_diem[i].get_so_diem() < self.bang_diem[j].get_so_diem():
                        self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
        for i in self.bang_diem:
            print(i)

    def main(self):
        while (1 == 1):
            print("\nCHUONG TRINH QUAN LY SINH VIEN")
            print("*****************************MENU******************************")
            print("**  1. Them sinh vien.                                       **")
            print("**  2. Them giao vien.                                       **")
            print("**  3. Them mon hoc.                                         **")
            print("**  4. Them lop hoc.                                         **")
            print("**  5. Them diem.                                            **")
            print("**  6. Sap xep bang diem tang dan theo ten, sau do den diem. **")
            print("**  7. Sap xep bang diem giam dan theo ten, sau do den diem. **")
            print("**  0. Thoat                                                 **")
            print("***************************************************************")

            key = int(input("Nhap tuy chon: "))
            if (key == 1):
                print("\n1. Them sinh vien.")
                self.them_sv()
                print("\nThem sinh vien thanh cong!")
            elif (key == 2):
                print("\n2. Them giao vien.")
                self.them_gv()
                print("\nThem giao vien thanh cong!")
            elif (key == 3):
                print("\n3. Them mon hoc.")
                self.them_mon()
                print("\nThem mon hoc thanh cong!")
            elif (key == 4):
                print("\n4. Them lop hoc.")
                self.them_lop()
                print("\nThem lop hoc thanh cong!")
            elif (key == 5):
                print("\n5. Them diem.")
                self.them_diem()
                print("\nThem diem thanh cong!")
            elif (key == 6):
                print("\n6. Sap xep bang diem tang dan theo ten, sau do den diem.")
                self.sap_xep_tang()
                print("\nSap xep tang dan thanh cong!")
            elif (key == 7):
                print("\n7. Sap xep bang diem giam dan theo ten, sau do den diem.")
                self.sap_xep_giam()
                print("\nSap xep giam dan thanh cong!")
            elif (key == 0):
                print("\nBan da chon thoat chuong trinh!")
                break
            else:
                print("\nKhong co chuc nang nay!")
                print("\nHay chon chuc nang trong hop menu.")

if __name__ == "__main__":   
   qlsv = QLSV()
   qlsv.main()