class Nguoi:
    
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi):
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._dia_chi = dia_chi

  class Nguoi:
    
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi):
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._dia_chi = dia_chi

    def getTen(self):
        return self._ten

    def getDiaChi(self):
        return self._dia_chi
    
    def getTuoi(self):
        return self._tuoi

    def getGioiTinh(self):
        return self._gioi_tinh

    @classmethod
    def nhap(cls):
        ten = input("Nhap ten: ")
        gioi_tinh = input("Nhap gioi tinh: ")
        tuoi = input("Nhap tuoi: ")
        dia_chi = input("Nhap dia chi: ")
        return Nguoi(ten, gioi_tinh, tuoi, dia_chi)
