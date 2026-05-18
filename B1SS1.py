print("-------- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --------")
name_patient = input("Nhập tên bệnh nhân: ")
age = int(input("Mời bạn nhập tuổi: "))
symptom = input("Mời bạn nhập triệu chứng bệnh ")

print("--- PHIẾU KHÁM BỆNH ---")
print("Tên bệnh nhân: ", name_patient) #Tên bệnh nhân phải là name_patien chứ không phải là symptom (symptom là tên triệu chứng)
print("Tuổi", age) #Tuổi trong chương trình đã cho sẵn đang bị sai kiểu dữ liệu / tuổi người dùng nhập vào được lưu vào biến age nhưng chương tình đã cho lại xuất dữ liệu chuỗi là name_patient
print("Triệu chứng", symptom) # Tương tự như tên và tuổi thì chương trình đã cho đang xuất ra sai kiểu dũ liệu của triệu chứng (symptom)
