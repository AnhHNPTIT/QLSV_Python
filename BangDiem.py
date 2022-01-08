class BangDiem:

    def __init__(self, sinh_vien, mon_hoc, so_diem):
        self._sinh_vien = sinh_vien
        self._mon_hoc = mon_hoc
        self._so_diem = so_diem

    def get_sinh_vien(self):
        return self._sinh_vien
    
    def get_so_diem(self):
        return self._so_diem
    
    def __repr__(self) -> str:
        return f"Ten sinh vien: {self._sinh_vien.getTen()} - Diem: {self._so_diem}"
