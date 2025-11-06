tuoi = 18
nhap_tuoi = int(input("Nhập số tuổi của bạn:"))
ma_so_sinh_vien = 25021512
mat_khau = 25021512 #mật khẩu tạm thời là mã số sinh viên1
if nhap_tuoi >= tuoi:
    print("Khách hàng đã đủ tuổi để thực hiện giao dịch. Vui lòng chuyển qua bước tiếp theo")
    nhap_ma_so_sinh_vien = int(input("Vui lòng nhập mã số sinh viên: "))
    if nhap_ma_so_sinh_vien == ma_so_sinh_vien:
        print("Sinh viên: Nguyễn Hữu Dũng.")
        print("Mã số sinh viên:", ma_so_sinh_vien,".")
    elif nhap_ma_so_sinh_vien != ma_so_sinh_vien:
        print("Mã số sinh viên không hợp lệ.")
    nhap_mat_khau = int(input("Nhập mật khẩu tài khoản của bạn:"))
    if nhap_mat_khau != mat_khau:
        print("Mật khẩu không hợp lệ. Vui lòng nhập lại")
    else:
        so_du = 100000000000000000000000
        while True:
            a = int(input("Nhập số tiền muốn rút:"))
            if a <= 0:
                print("Số tiền không hợp lệ. Vui lòng nhập lại.")
                continue
            elif a > so_du:
                print("Số dư không khả dụng.")
                continue
            elif a % 1000 != 0:
                print("Sô tiền không hợp lệ. Vui lòng nhập lại")
            else:
                break
        print("Số tiền nhập vào hợp lệ")
        print("Số tiền",a,"của quý khách đang được xử lý")
else:
    print("Quý khách chưa đủ tuổi để thực hiện giao dịch")
 