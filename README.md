<center>
    <h3>BỘ GIÁO DỤC VÀ ĐÀO TẠO</h3>
    <h3>TRƯỜNG ĐẠI HỌC MỎ - ĐỊA CHẤT</h3>
    <img src="img/logo_humg.jpg" height="200px" width="200px">
    <br>
    <h2>ĐỀ TÀI: “XÂY DỰNG MÔ HÌNH HỌC MÁY DỰ ĐOÁN BỆNH TIM”</h2>
</center>


Trưởng nhóm nghiên cứu: **Nguyễn Văn Huy, Lớp DCCTCLC66A1** </br></br>
Thành viên tham gia thực hiện:</br>
**1. Mai Thị Diễm, DCCTCLC66A1**<br>
**2. Nguyễn Hoàng Tùng Phong, DCCTCLC66A1**</br></br>
Giáo viên hướng dẫn: **Thạc Sĩ Đặng Văn Nam**


## Mục tiêu đề tài:

Mục tiêu của đề tài là xây dựng và đánh giá hiệu suất của một mô hình học máy có khả năng dự đoán bệnh tim dựa trên tập dữ liệu HeartDisease. Cụ thể, các mục tiêu chính bao gồm:
* **Thu thập và Tiền Xử Lý Dữ Liệu:** Tập trung vào việc thu thập dữ liệu từ tập dữ liệu HeartDisease và tiền xử lý các dữ liệu này để chuẩn bị cho quá trình huấn luyện mô hình. Bước này bao gồm xử lý dữ liệu thiếu, mã hóa các biến phân loại và chuẩn hóa các biến số.
* **Xây Dựng Mô Hình Học Máy:** Phát triển và tinh chỉnh các mô hình học máy để dự đoán nguy cơ mắc bệnh tim dựa trên các đặc điểm lâm sàng của bệnh nhân. Một loạt các thuật toán học máy sẽ được thử nghiệm, bao gồm các mô hình cổ điển như Random Forest, K-Nearest Neighbors (KNN), Decision Tree.
* **Đánh Giá Hiệu Suất:** Đánh giá hiệu suất của các mô hình được xây dựng bằng cách sử dụng các phương pháp đánh giá chuẩn, bao gồm ma trận nhầm lẫn, 
* **So Sánh và Lựa Chọn Mô Hình Tốt Nhất:** So sánh hiệu suất của các mô hình khác nhau và lựa chọn mô hình tốt nhất dựa trên các tiêu chí như độ chính xác, độ nhạy và độ đặc hiệu. Mô hình được chọn sẽ được xem xét là phù hợp nhất để dự đoán bệnh tim từ các biến số lâm sàng.

Bằng cách hoàn thành các mục tiêu này, đề tài nghiên cứu này nhằm cung cấp một cách tiếp cận hiệu quả và đáng tin cậy để dự đoán bệnh tim dựa trên dữ liệu lâm sàng, đóng góp vào nỗ lực chung trong việc cải thiện sức khỏe cộng đồng và chăm sóc cá nhân. 

## Giới thiệu về bộ dữ liệu:
Bộ dữ liệu ban đầu đến từ <a href="https://www.cdc.gov/heartdisease/risk_factors.htm" target="_blank">CDC</a>
  và là một phần chính của Hệ thống giám sát yếu tố rủi ro hành vi (BRFSS), thực hiện khảo sát qua điện thoại hàng năm để thu thập dữ liệu về tình trạng sức khỏe của cư dân Hoa Kỳ. Theo mô tả của CDC: Được thành lập vào năm 1984 với 15 tiểu bang, BRFSS hiện thu thập dữ liệu ở tất cả 50 tiểu bang, Quận Columbia và ba vùng lãnh thổ của Hoa Kỳ. BRFSS hoàn thành hơn 400.000 cuộc phỏng vấn người lớn mỗi năm, trở thành cuộc phỏng vấn sức khỏe được tiến hành liên tục lớn nhất hệ thống khảo sát trên thế giới tập dữ liệu gần đây nhất bao gồm dữ liệu từ năm 2022. Nó bao gồm 445.134 hàng và 41 cột. Phần lớn các cột là những câu hỏi được đặt ra cho người trả lời về tình trạng sức khỏe của họ, chẳng hạn như “Bạn có gặp khó khăn nghiêm trọng khi đi bộ hoặc leo cầu thang không?” hoặc “Bạn có hút thuốc lá không (nếu có mức độ như nào)?”.
</br>
Trong tập dữ liệu này, chúng em nhận thấy nhiều yếu tố (câu hỏi) khác nhau ảnh hưởng trực tiếp hoặc gián tiếp đến bệnh tim, vì vậy chúng em quyết định chọn các biến có liên quan nhất từ nó và thực hiện một số làm sạch để nó có thể sử dụng được cho các dự án.
</br>
Tập dữ liệu HeartDisease bao gồm 445.133  bản ghi và 40 thuộc tính.
</br>


**21 thuộc tính sau được sử dụng trong quá trình phân tích và xây dựng mô hình học máy:**

- **Sex:** Giới tính của cá nhân --Sx
- **GeneralHealth:** Tình trạng sức khỏe tổng thể của cá nhân -- Gh
- **PhysicalHealthDays:** Số ngày trong năm mà cá nhân cảm thấy sức khỏe thể chất của họ kém --Phd
- **MentalHealthDays:** Số ngày trong năm mà cá nhân cảm thấy sức khỏe tinh thần của họ kém --Mhd
- **PhysicalActivities:** Mức độ hoạt động thể chất của cá nhân --Pa
- **SleepHours:** Số giờ ngủ trung bình mỗi đêm của cá nhân --Slh
- **HadHeartAttack:** Cá nhân có bị đau tim hay không --hd
- **HadStroke:** Cá nhân đã từng bị đột quỵ hay chưa --Hs
- **HadAsthma:** Cá nhân đã từng bị hen suyễn hay chưa --Has
- **HadSkinCancer:** Cá nhân đã từng bị ung thư da hay chưa --Hsc
- **HadDepressiveDisorder:** Cá nhân đã từng bị rối loạn trầm cảm hay chưa --Hd
- **HadKidneyDisease:** Cá nhân đã từng bị bệnh thận hay chưa --Hkd
- **HadArthritis:** Cá nhân đã từng bị viêm khớp hay chưa --Har
- **HadDiabetes:** Cá nhân đã từng bị tiểu đường hay chưa --Hdi
- **DifficultyWalking:** Cá nhân có khó khăn khi đi bộ hay không --Dw
- **SmokerStatus:** Tình trạng hút thuốc của cá nhân --Sst
- **RaceEthnicityCategory:** Thuộc chủng tộc/dân tộc --Rec
- **AgeCategory:** Nhóm tuổi của cá nhân --Ac
- **BMI:** Chỉ số cơ thể của cá nhân --BMI
- **AlcoholDrinkers:** Cá nhân có uống rượu bia hay không --Adr
- **CovidPos:** Cá nhân đã từng mắc COVID-19 hay chưa --CovidPos

## Bản quyền

© 2025 **Nguyễn Văn Huy** và các thành viên nhóm **Mai Thị Diễm**, **Nguyễn Hoàng Tùng Phong**. Mọi quyền được bảo lưu.  
Dự án được thực hiện phục vụ mục đích học tập và nghiên cứu tại **Trường Đại học Mỏ - Địa chất**.  
