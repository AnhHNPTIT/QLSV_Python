""" Xây dựng chương trình cho phép nhập dữ liệu là các đối tượng của các lớp trên từ bàn phím
    Thực hiện sắp xếp danh sách các đối tượng này theo chiều tăng dần (hoặc giảm dần) trên 1 hoặc nhiều thuộc tính của đối tượng"""

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

    def nhap(self):
        print ("nhap")
        input()

    def sap_xep(self):
        print ("sap_xep")
        # vowels list
        vowels = ['e', 'a', 'u', 'o', 'i']
        # sort the vowels
        vowels.sort(reverse=True)

if __name__ == '__main__':
    ng = Nguoi()

