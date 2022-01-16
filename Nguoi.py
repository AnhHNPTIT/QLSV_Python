class Nguoi:
    
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi):
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._dia_chi = dia_chi

    def get_ten(self):
        return self._ten

    def get_dia_chi(self):
        return self._dia_chi
    
    def get_tuoi(self):
        return self._tuoi

    def get_gioi_tinh(self):
        return self._gioi_tinh

    @classmethod
    def nhap(cls):
        ten = input("Nhap ten: ")
        gioi_tinh = input("Nhap gioi tinh: ")
        tuoi = input("Nhap tuoi: ")
        dia_chi = input("Nhap dia chi: ")
        return Nguoi(ten, gioi_tinh, tuoi, dia_chi)
