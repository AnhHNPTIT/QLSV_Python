
class Diem:

    def __init__(self, ma_sinh_vien, ma_mon_hoc, so_diem):
        self._ma_sinh_vien = ma_sinh_vien
        self._ma_mon_hoc = ma_mon_hoc
        self._so_diem = so_diem

    @classmethod
    def nhap(cls):
        ma_sv = input("Nhap ma sinh vien: ")
        ma_mon_hoc = input("Nhap ma mon hoc: ")
        diem = input("Nhap so diem: ")
        return Diem(ma_sv, ma_mon_hoc, diem)
    
    def get_ma_sinh_vien(self):
        return self._ma_sinh_vien
    
    def get_so_diem(self):
        return self._so_diem
    
    def get_ma_mon_hoc(self):
        return self._ma_mon_hoc
    
    def __repr__(self):
        return '{' + self.get_ma_sinh_vien() + ', ' + self.get_ma_mon_hoc() + ', ' + str(self.get_so_diem()) + '}'


if __name__ == "__main__":
    print("_____Nhap diem______")
    d1 = Diem.nhap()
    print("_____Nhap diem______")
    d2 = Diem.nhap()
    print("_____Nhap diem______")
    d3 = Diem.nhap()

    bang_diem = [d1, d2, d3]
    # 1. Sap xep theo ma sinh vien tang dan
    bang_diem.sort(key=lambda x: x.get_ma_sinh_vien())
    print(bang_diem)

    # 2. Sap xep theo so diem giam dan
    bang_diem.sort(key=lambda x: float(x.get_so_diem()), reverse=True)
    print(bang_diem)