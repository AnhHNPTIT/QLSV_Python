from Nguoi import Nguoi


class SinhVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_sv, chuyen_nganh):
        super().__init__(ten, gioi_tinh, tuoi, dia_chi)
        self._ma_sv = ma_sv
        self._chuyen_nganh = chuyen_nganh

    def get_ma(self):
        return self._ma_sv

    def get_chuyen_nganh(self):
        return self._chuyen_nganh

    def __repr__(self) -> str:
        return f"Ma sinh vien: {self._ma_sv} - Ten: {self._ten} - Chuyen nganh: {self._chuyen_nganh}"