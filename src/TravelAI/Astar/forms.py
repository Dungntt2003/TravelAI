from django import forms


# nameOfCity = ["Tay Ninh", "Vung Tau", "Ben Tre", "Phu Quoc", "TP Ho Chi Minh", "Nha Trang", "Dong Thap", 
# "Can Tho", "Soc Trang", "Ca Mau", "Lang Son", "Cao Bang", "Ha Giang", "Lao Cai","Lai Chau", "Dien Bien", 
# "Son La", "Phu Tho", "Ha Noi", "Quang Ninh", "Hai Duong", "Hai Phong", "Thai Binh", "Nam Dinh", "Ninh Binh", 
# "Thanh Hoa", "Nghe An", "Quang Binh", "Hue", "Da Nang"]


class MyForm(forms.Form):
    choice1 = (
        ('', "Chọn"),
        ('Tay Ninh' , "Tây Ninh"),
        ('Vung Tau', 'Vũng Tàu'),
        ('Ben Tre', 'Bến Tre'),
        ('Phu Quoc', 'Phú Quốc'),
        ('TP Ho Chi Minh', 'TP Hồ Chí Minh'),
        ('Nha Trang', 'Nha Trang'),
        ('Dong Thap', 'Đồng Tháp'),
        ('Can Tho', 'Cần Thơ'),
        ('Soc Trang', 'Sóc Trăng'),
        ('Ca Mau', 'Cà Mau'),
        ('Lang Son', 'Lạng Sơn'),
        ('Cao Bang', 'Cao Bang'),
        ('Ha Giang', 'Hà Giang'),
        ('Lao Cai', 'Lào Cai'),
        ('Lai Chau', 'Lai Châu'),
        ('Dien Bien', 'Điện Biên'),
        ('Son La', 'Sơn La'),
        ('Phu Tho', 'Phú Thọ'),
        ('Ha Noi', 'Hà Nội'),
        ('Quang Ninh', 'Quảng Ninh'),
        ('Hai Duong', 'Hải Dương'),
        ('Hai Phong', 'Hải Phòng'),
        ('Thai Binh', 'Thái Bình'),
        ('Nam Dinh', 'Nam Định'),
        ('Ninh Binh', 'Ninh Bình'),
        ('Thanh Hoa', 'Thanh Hóa'),
        ('Nghe An', 'Nghệ An'),
        ('Quang Binh', 'Quảng Bình'),
        ('Hue', 'Huế'),
        ('Da Nang', 'Đà Nẵng'),
    )

    choice2 = (
        ('', 'Chọn'),
        ('Tay Ninh' , "Tây Ninh"),
        ('Vung Tau', 'Vũng Tàu'),
        ('Ben Tre', 'Bến Tre'),
        ('Phu Quoc', 'Phú Quốc'),
        ('TP Ho Chi Minh', 'TP Hồ Chí Minh'),
        ('Nha Trang', 'Nha Trang'),
        ('Dong Thap', 'Đồng Tháp'),
        ('Can Tho', 'Cần Thơ'),
        ('Soc Trang', 'Sóc Trăng'),
        ('Ca Mau', 'Cà Mau'),
        ('Lang Son', 'Lạng Sơn'),
        ('Cao Bang', 'Cao Bang'),
        ('Ha Giang', 'Hà Giang'),
        ('Lao Cai', 'Lào Cai'),
        ('Lai Chau', 'Lai Châu'),
        ('Dien Bien', 'Điện Biên'),
        ('Son La', 'Sơn La'),
        ('Phu Tho', 'Phú Thọ'),
        ('Ha Noi', 'Hà Nội'),
        ('Quang Ninh', 'Quảng Ninh'),
        ('Hai Duong', 'Hải Dương'),
        ('Hai Phong', 'Hải Phòng'),
        ('Thai Binh', 'Thái Bình'),
        ('Nam Dinh', 'Nam Định'),
        ('Ninh Binh', 'Ninh Bình'),
        ('Thanh Hoa', 'Thanh Hóa'),
        ('Nghe An', 'Nghệ An'),
        ('Quang Binh', 'Quảng Bình'),
        ('Hue', 'Huế'),
        ('Da Nang', 'Đà Nẵng'),
    )
    startCity = forms.ChoiceField(choices=choice1, label='Chọn thành phố bắt đầu', initial='')
    endCity = forms.ChoiceField(choices=choice2, label='Chọn thành phố kết thúc', initial='')


