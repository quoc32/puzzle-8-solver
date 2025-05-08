Họ Tên Sinh Viên: Vũ Anh Quốc
Mã số sinh viên: 23110296

BÁO CÁO CÁ NHÂN
Môn học: TRÍ TUỆ NHÂN TẠO
Chủ đề: Giải bài toán 8 ô chữ với các thuật toán AI cơ bản


 

1. Giải với thuật toán BFS
 ![image](https://github.com/user-attachments/assets/989d1995-01b5-4b74-9486-c2802f3f92a2)

-	Giao diện: 
+ Nút Random để tạo 1 bảng ngẫu nhiên.
+ Nút Solve để giải.
+ Nút View để xem sơ đồ cây của giải thuật.
 ![image](https://github.com/user-attachments/assets/6e74529f-e776-4768-a2c0-081e72bfe267)

-	Ta có thể thấy biểu đồ cây của giải thuật bfs mở rộng theo chiều ngang rất nhiều.
 ![image](https://github.com/user-attachments/assets/e87b0ddf-f08b-422a-844f-a4f3e50bb98a)

-	Node thúc và khởi đầu có màu xanh lá.
  ![image](https://github.com/user-attachments/assets/6b53fe99-5f5c-4a7b-a90b-96e8899f40d0)

 
2. Giải với thuật toán DFS
 
![image](https://github.com/user-attachments/assets/d445e6f9-c6e6-4e70-b2c2-9b8f17eccfa6)

-	Giao diện: 
+ Nút Random để tạo 1 bảng ngẫu nhiên.
+ Nút Solve để giải.
+ Nút View để xem sơ đồ cây của giải thuật.
![image](https://github.com/user-attachments/assets/84c3d0b4-4195-4e19-80bd-491c47fc3eb3)

 ![image](https://github.com/user-attachments/assets/7dd386fb-135c-4fe9-a5e4-01a19426fd6d)

 ![image](https://github.com/user-attachments/assets/64194433-bebf-420b-a443-4caa02b8834e)

-	Nhận xét: Biểu đồ cây của giải thuật DSF được mở rộng theo chiều sâu rất nhiều.
  ![image](https://github.com/user-attachments/assets/038277dd-2e5b-4e33-bf96-8ef030757864)

 
3. Giải với thuật toán IDS
   ![image](https://github.com/user-attachments/assets/d2d92fbd-c4d0-4bfa-8293-16330c9bc0c8)

-	IDS: Hàm giải thuật toán này được code với ngôn ngữ c++ nên nó chạy rất nhanh và nhẹ, tuy nhiên nó không generation ra biểu đồ cây.
  ![image](https://github.com/user-attachments/assets/690f72a7-aebf-4ffe-93ae-7f7005cc1a38)

 
4. Giải với thuật toán A*
 ![image](https://github.com/user-attachments/assets/809924e6-11c2-4e22-bb8e-7f88d1c16d90)

 
-	Đây là hình dạng tổng thể cây của giải thuật.
 ![image](https://github.com/user-attachments/assets/65f0fd8a-867c-42c7-9f17-4f67dc8b2b63)

 ![image](https://github.com/user-attachments/assets/eb8abdc7-cbbf-426b-8e56-d65c213a9730)
![image](https://github.com/user-attachments/assets/ef700e01-89ca-48bb-8fdc-8376b4eceb7b)

 ![image](https://github.com/user-attachments/assets/42b036c8-e3ed-448e-bc69-dc0e321243ec)

- Nhận xét: nhìn chung cây cũng được mở rộng theo chiều ngang rất nhiều khi so sánh với giải thuật tham lam (greedy), nhưng có phần cân đối hơn so với bfs.
5. Giải với thuật toán tham lam (Greedy)
 
 ![image](https://github.com/user-attachments/assets/993f9b19-4668-4135-9133-15971b759706)
![image](https://github.com/user-attachments/assets/d73b56f1-7f53-49e2-8915-42ac5f1e8089)

 
-	Nhận xét: hình dạng cây của giải thuật khá cân bằng, vừa được mở rộng theo chiều ngang và chiều sâu 1 cách cân đối, xét về phương diện thời gian, tôi đánh giá đây là giait thuật tốt nhất để giải, tuy nhiên, nếu bạn cần lời giải tối ưu nhất, thì bfs là lựa chọn tốt nhất.
 
 ![image](https://github.com/user-attachments/assets/f275a6bb-8d8a-487f-a4da-bc8f05bf31d8)
 ![image](https://github.com/user-attachments/assets/a3230be5-7271-4e7a-8fa6-66741c82f2e1)
![image](https://github.com/user-attachments/assets/9c2d105b-9b9d-40a2-8222-cb5665155e30)

![image](https://github.com/user-attachments/assets/b332d91d-8fe8-412a-ba3f-e5377838c76c)

 
6. Giải với thuật toán IDA*

7. Giải với thuật toán tìm kiếm thế hệ (Generation Search)
 ![image](https://github.com/user-attachments/assets/07cb2e3b-0223-4f7c-988b-aa4426dc6d2f)

-	Menu chức năng: gồm 2 phần, chạy giải thuật và xem map.
  ![image](https://github.com/user-attachments/assets/354e0857-7b16-422a-b131-337de7ba9179)

 
-	Sau khi chạy giải thuật, thông tin của các thế hệ được sinh ra để được lưu trong thư mục data.
  ![image](https://github.com/user-attachments/assets/f31bf957-3745-4f88-b3f6-39da49524f55)

 
-	Đây là ví dụ thông tin của 1 thế hệ, bao gồm giá trị của cá thể và giá trị fitness của có thể đó.
  ![image](https://github.com/user-attachments/assets/76d973b6-01e9-4c46-993f-08e3b7b57b98)

 
-	Đây là view map để xem thông tin và hình ảnh trực quan của mỗi thế hệ, thế hệ ban đầu (gen 0) là được random ngẫu nhiên.
  ![image](https://github.com/user-attachments/assets/f86800a5-7d84-4059-a997-87bebb4dc5bc)

 
-	Các thế hệ sau được sinh sản và chọn lọc nên dần dần có giá trị fitness trung bình cho quần thể ngày 1 cải thiện.
 
 ![image](https://github.com/user-attachments/assets/754c97dd-d629-4542-92b1-857dea02d567)
 ![image](https://github.com/user-attachments/assets/4ccfbcc6-abf8-4241-8bdd-b7fc9b9c7e97)
![image](https://github.com/user-attachments/assets/1540604e-869a-44cb-8452-ba8faae06a3a)
![image](https://github.com/user-attachments/assets/faaeedce-cf8d-4883-8dd8-b9c64d3e5ad5)
![image](https://github.com/user-attachments/assets/f08ea97a-0837-455a-a00e-d78a7023b73d)


- Quá trình chọn lọc và sinh sản được diễn ra cho đến khi cá thể có fitness 0 được tìm thấy.
8. Giải với thuật toán leo đồi đơn giản (Simple Hill Climbing)
 ![image](https://github.com/user-attachments/assets/d5514743-17ca-45e8-8889-6aa4abd1fb86)
![image](https://github.com/user-attachments/assets/b46882e1-7d9d-40ac-aace-34980f9175fd)

 

9. Giải với thuật toán leo đồi ngẫu nhiên (Random Hill Climbing)
 ![image](https://github.com/user-attachments/assets/a43804c1-9d74-422f-a9c2-c79c68332249)

10. Giải với thuật toán leo đồi dốc nhất (Steepest Ascent Hill Climbing)
 ![image](https://github.com/user-attachments/assets/dba20c34-8ea8-4eef-b1cf-900362767c70)

11. Giải với thuật toán Beam Search
 ![image](https://github.com/user-attachments/assets/6a87474d-17c1-4b10-a8e9-739d8b589bcf)

 ![image](https://github.com/user-attachments/assets/ee34d155-90a2-49de-bebe-a8fbcef00b46)

12. Giải với thuật toán tôi thép (Simulated Annealing)

 ![Uploading image.png…]()

 
 
