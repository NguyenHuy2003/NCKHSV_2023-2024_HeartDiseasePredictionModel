# import các thư viện cần thiết
import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

# Tạo ứng dụng Flask
app = Flask(__name__)

# Load mô hình đã huấn luyện
filemodel = 'model/heart_disease_model.sav'
KNN = pickle.load(open(filemodel, 'rb'))

# Cấu hình môi trường và debug mode
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True

# Định nghĩa trang chủ
@app.route('/')
def index():
    return render_template('index.html')

# Xử lý dự đoán khi nhận dữ liệu từ giao diện người dùng
@app.route('/predict', methods=['POST'])
def predict():
    
        # Lấy dữ liệu từ biểu mẫu gửi từ giao diện người dùng
        sex = int(request.form['sex'])  # Giới tính
        general_health = int(request.form['general_health'])  # Tình trạng sức khỏe tổng thể
        physical_health_days = int(request.form['physical_health_days'])  # Số ngày cảm thấy sức khỏe thể chất kém
        mental_health_days = int(request.form['mental_health_days'])  # Số ngày cảm thấy sức khỏe tinh thần kém
        physical_activities = int(request.form['physical_activities'])  # Hoạt động thể chất
        sleep_hours = int(request.form['sleep_hours'])  # Số giờ ngủ trung bình mỗi đêm
        had_stroke = int(request.form['had_stroke'])  # Đã từng bị đột quỵ
        had_asthma = int(request.form['had_asthma'])  # Đã từng bị hen suyễn
        had_skin_cancer = int(request.form['had_skin_cancer'])  # Đã từng bị ung thư da
        had_depressive_disorder = int(request.form['had_depressive_disorder'])  # Đã từng bị rối loạn trầm cảm
        had_kidney_disease = int(request.form['had_kidney_disease'])  # Đã từng bị bệnh thận
        had_arthritis = int(request.form['had_arthritis'])  # Đã từng bị viêm khớp
        had_diabetes = int(request.form['had_diabetes'])  # Đã từng bị tiểu đường
        difficulty_walking = int(request.form['difficulty_walking'])  # Có khó khăn khi đi bộ
        smoker_status = int(request.form['smoker_status'])  # Tình trạng hút thuốc
        race_ethnicity_category = int(request.form['race_ethnicity_category'])  # Chủng tộc/dân tộc
        age_category = int(request.form['age_category'])  # Nhóm tuổi
        bmi = int(request.form['bmi'])  # Chỉ số BMI
        alcohol_drinkers = int(request.form['alcohol_drinkers'])  # Uống rượu bia
        covid_pos = int(request.form['covid_pos'])  # Đã từng mắc COVID-19
        
        # Lấy giá trị từ các checkboxes
        # Lấy danh sách các giá trị được chọn từ checkboxes
        selected_checkboxes = request.form.getlist('your_checkbox_name')

        # Kiểm tra xem checkbox nào đã được chọn và xử lý dữ liệu tương ứng
        # Ví dụ:
        if 'value1' in selected_checkboxes:
            # Xử lý khi checkbox có giá trị 'value1' được chọn
            pass
        if 'value2' in selected_checkboxes:
            # Xử lý khi checkbox có giá trị 'value2' được chọn
            pass

        # Dự đoán bệnh tim
        data = np.array([[sex, general_health, physical_health_days, mental_health_days, physical_activities,
                          sleep_hours, had_stroke, had_asthma, had_skin_cancer, had_depressive_disorder,
                          had_kidney_disease, had_arthritis, had_diabetes, difficulty_walking, smoker_status,
                          race_ethnicity_category, age_category, bmi, alcohol_drinkers, covid_pos]])
        prediction = KNN.predict(data)

        # Chuẩn bị kết quả dự đoán
        if prediction == 0:
            result = "AI dự đoán: Bạn không mắc bệnh tim!"
        else:
            result = "AI dự đoán: Bạn có khả năng mắc bệnh tim!"

        # Trả về template với kết quả dự đoán
        return render_template('index.html', result=result)
    


if __name__ == '__main__':
    # Cấu hình host và port
    app.run()
