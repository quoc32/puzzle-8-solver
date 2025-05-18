Họ Tên Sinh Viên: Vũ Anh Quốc

Mã số sinh viên: 23110296

# BÁO CÁO CÁ NHÂN
Môn học: TRÍ TUỆ NHÂN TẠO

Chủ đề: Giải bài toán 8 ô chữ với các thuật toán AI cơ bản


 
# 1.	Giải với thuật toán BFS
- BFS là một thuật toán duyệt đồ thị hoặc cây theo từng lớp (layer), tức là:
•	Duyệt tất cả đỉnh kề với đỉnh hiện tại trước.
•	Sau đó mới duyệt đến các đỉnh xa hơn 1 bước.
- Ý tưởng chính của BFS:
•	Sử dụng một hàng đợi (queue) để duyệt các đỉnh theo thứ tự chiều rộng.
•	Bắt đầu từ đỉnh xuất phát:
o	Đưa vào queue
o	Đánh dấu đã thăm
o	Duyệt từng đỉnh kề và lặp lại quy trình


 
-	Giao diện: 
+ Nút Random để tạo 1 bảng ngẫu nhiên.
+ Nút Solve để giải.
+ Nút View để xem sơ đồ cây của giải thuật.
 
-	Ta có thể thấy biểu đồ cây của giải thuật bfs mở rộng theo chiều ngang rất nhiều.
 
-	Node thúc và khởi đầu có màu xanh lá.
 
# 2. Giải với thuật toán DFS
- DFS là thuật toán duyệt cây hoặc đồ thị bằng cách đi sâu nhất có thể theo một nhánh, sau đó mới quay lại để duyệt các nhánh khác.
Khác với BFS (chiều rộng), DFS ưu tiên chiều sâu.
- Ý tưởng chính của DFS:
+ Bắt đầu từ đỉnh xuất phát.
+ Đánh dấu đỉnh là đã thăm.
+ Duyệt đệ quy hoặc sử dụng stack để đến đỉnh kề chưa thăm.
+ Khi không còn đỉnh nào đi được → quay lui.

 

-	Giao diện: 
+ Nút Random để tạo 1 bảng ngẫu nhiên.
+ Nút Solve để giải.
+ Nút View để xem sơ đồ cây của giải thuật.

 
(Hình ảnh các node ban đầu)
 
(Hình ảnh tổng thể của cây)
 
-	Nhận xét: Biểu đồ cây của giải thuật DSF được mở rộng theo chiều sâu rất nhiều.
 
(Hình ảnh các node cuối của cây)

# 3. Giải với thuật toán IDS
 
-	IDS: Hàm giải thuật toán này được code với ngôn ngữ c++ nên nó chạy rất nhanh và nhẹ, tuy nhiên nó không generation ra biểu đồ cây.
 
# 4. Giải với thuật toán A*
- A* là một thuật toán tìm đường đi ngắn nhất trên đồ thị, kết hợp giữa:
•	Tính chính xác của Dijkstra (tìm đường tối ưu).
•	Tính hiệu quả của Greedy Best-First Search (tìm nhanh hướng về đích).
- Nó là informed search algorithm – sử dụng hàm heuristic để dự đoán chi phí còn lại đến đích.

 
 
-	Đây là hình dạng tổng thể cây của giải thuật.
 
 
 
- Nhận xét: nhìn chung cây cũng được mở rộng theo chiều ngang rất nhiều khi so sánh với giải thuật tham lam (greedy), nhưng có phần cân đối hơn so với bfs.
# 5. Giải với thuật toán tham lam (Greedy)
- Thuật toán tham lam là một kỹ thuật giải bài toán bằng cách:
Luôn chọn phương án tốt nhất tại mỗi bước với hy vọng rằng toàn bộ lời giải sẽ tối ưu toàn cục.
Tức là:
•	Không xét lại các lựa chọn trước đó.
•	Không quay lui như backtracking, không thử mọi khả năng như Brute Force.

 
 
 
- Nhận xét: hình dạng cây của giải thuật khá cân bằng, vừa được mở rộng theo chiều ngang và chiều sâu 1 cách cân đối, xét về phương diện thời gian, tôi đánh giá đây là giait thuật tốt nhất để giải, tuy nhiên, nếu bạn cần lời giải tối ưu nhất, thì bfs là lựa chọn tốt nhất.
 

 
 
# 6. Giải với thuật toán IDA*

# 7. Giải với thuật toán tìm kiếm thế hệ (Generation Search)
- Thuật toán Tìm kiếm theo thế hệ là một kỹ thuật tối ưu hóa mô phỏng quá trình tiến hóa tự nhiên của sinh vật. Nó dựa trên di truyền học, đột biến, lai ghép và chọn lọc tự nhiên. 
- GA là một dạng của thuật toán tiến hóa (evolutionary algorithm) và rất hiệu quả trong các bài toán tìm kiếm không gian lớn, phức tạp.
- Ý tưởng chính:
+ Mã hóa lời giải thành cá thể (gen/chromosome).
+ Khởi tạo quần thể (population) ngẫu nhiên.
+ Lặp qua các thế hệ:
o	Đánh giá độ tốt (fitness) của từng cá thể.
o	Chọn lọc các cá thể tốt để lai ghép (crossover).
o	Áp dụng đột biến (mutation) để tạo sự đa dạng.
o	Hình thành quần thể mới.
+ Lặp lại cho đến khi tìm được lời giải tốt hoặc đạt số thế hệ tối đa.

 
- Menu chức năng: gồm 2 phần, chạy giải thuật và xem map.
 
- Sau khi chạy giải thuật, thông tin của các thế hệ được sinh ra để được lưu trong thư mục data.
 
- Đây là ví dụ thông tin của 1 thế hệ, bao gồm giá trị của cá thể và giá trị fitness của có thể đó.
 
- Đây là view map để xem thông tin và hình ảnh trực quan của mỗi thế hệ, thế hệ ban đầu (gen 0) là được random ngẫu nhiên.
 
- Các thế hệ sau được sinh sản và chọn lọc nên dần dần có giá trị fitness trung bình cho quần thể ngày 1 cải thiện.
 
 
 
 
 
- Quá trình chọn lọc và sinh sản được diễn ra cho đến khi cá thể có fitness 0 được tìm thấy.
# 8. Giải với thuật toán leo đồi đơn giản (Simple Hill Climbing)
- Hill Climbing (leo đồi) là một thuật toán tìm kiếm địa phương (local search), thường dùng để tìm cực trị (cực đại hoặc cực tiểu) của một hàm mục tiêu bằng cách:
- Luôn di chuyển đến trạng thái láng giềng tốt hơn, lặp lại cho đến khi không còn trạng thái nào tốt hơn.
- Ý tưởng chính:
1.	Bắt đầu từ một trạng thái khởi đầu (start state).
2.	Tìm tất cả trạng thái láng giềng (neighbors).
3.	Chọn trạng thái láng giềng có giá trị hàm mục tiêu tốt nhất.
4.	Nếu trạng thái láng giềng tốt hơn trạng thái hiện tại → di chuyển đến nó.
5.	Lặp lại từ bước 2.
6.	Nếu không còn trạng thái láng giềng nào tốt hơn → dừng, trả về trạng thái hiện tại.


 
- Menu chọn các chức năng.
 

# 9. Giải với thuật toán leo đồi ngẫu nhiên (Random Hill Climbing)
- Đây là một biến thể của Hill Climbing truyền thống, nhằm khắc phục nhược điểm dễ bị kẹt ở cực trị địa phương bằng cách:
- Chọn ngẫu nhiên một trạng thái láng giềng thay vì luôn chọn láng giềng tốt nhất.

 
# 10. Giải với thuật toán leo đồi dốc nhất (Steepest Ascent Hill Climbing)
- Đây là một biến thể của thuật toán Hill Climbing, trong đó:
- Tại mỗi bước, thuật toán sẽ tìm và chọn trạng thái láng giềng tốt nhất (có giá trị hàm mục tiêu cao nhất) trong tất cả các láng giềng, rồi di chuyển đến trạng thái đó.
- Khác với Hill Climbing đơn giản (chọn láng giềng tốt hơn đầu tiên gặp), thuật toán này duyệt hết tất cả láng giềng rồi mới chọn láng giềng tốt nhất.

 
# 11. Giải với thuật toán Beam Search
- Beam Search là một thuật toán tìm kiếm heuristic, kết hợp giữa tìm kiếm theo chiều rộng (BFS) và lọc bớt các trạng thái không tốt dựa trên một tham số gọi là beam width (bề rộng chùm tia).
+ Thay vì giữ tất cả các nút con như BFS, Beam Search chỉ giữ lại một số lượng giới hạn các nút tốt nhất (theo đánh giá heuristic) ở mỗi bước.
+ Mục đích: Giảm bớt bộ nhớ và độ phức tạp tính toán so với BFS, đồng thời vẫn giữ đa dạng các lựa chọn tốt.

 
 
# 12. Giải với thuật toán tôi thép (Simulated Annealing)
- Simulated Annealing là một thuật toán tối ưu hóa heuristic (gần đúng) mô phỏng quá trình ủ nhiệt trong luyện kim – nơi kim loại được nung nóng và làm nguội dần để đạt được cấu trúc ổn định có năng lượng thấp nhất.
- Mục tiêu của SA: Tìm được nghiệm tối ưu gần nhất (gần toàn cục) cho các bài toán tối ưu hóa phức tạp, có không gian tìm kiếm rất lớn, dễ bị kẹt ở cực trị địa phương (local minimum).
- Ý tưởng chính:
•	Bắt đầu từ một nghiệm ban đầu.
•	Thực hiện hoán đổi nhỏ để tạo nghiệm mới.
•	Nếu nghiệm mới tốt hơn → chấp nhận.
•	Nếu nghiệm mới xấu hơn → vẫn có xác suất chấp nhận, phụ thuộc vào nhiệt độ T.
•	Nhiệt độ giảm dần theo thời gian (như làm nguội kim loại).

 
- Hình trên thể hiện việc thuật toán đã duyệt qua các node có giá trị heurictic không tốt hơn trong thời gian ban đầu và khi nhiệt độ ngày càng giảm, nó dừng lại và không tìm ra kết quả.
 
- Node trên cùn là trạng thái ban đầu.
 
- Không thể tìm đến đích do bị kẹt cục bộ.
# 13. Giải với thuật toán Backtracking
- Thuật toán Backtracking (quay lui) là một phương pháp tìm kiếm tổng quát để giải quyết các bài toán bằng cách thử từng khả năng, quay lại (backtrack) khi thấy một hướng đi không dẫn đến kết quả đúng.
- Ý tưởng chính của Backtracking:
+  Thử một cách chọn (bước đi).
+ Kiểm tra nếu cách chọn đó hợp lệ: Nếu đúng - tiếp tục thử bước tiếp theo. Nếu sai: quay lui và thử cách chọn khác.
+ Lặp lại quá trình trên cho đến khi: Tìm được lời giải (hoặc tất cả lời giải). Hoặc không còn khả năng nào hợp lệ.
 
- Đây là kết quả của bài toán 8 ô chữ khi giải bằng thuật toán Backtracking với ràng buộc “các giá trị của ô chữ phải liên tục tăng”.
# 14. Lọc Domain giá trị với thuật toán AC-3
- Thuật toán AC-3 (Arc Consistency Algorithm 3) là một thuật toán lọc ràng buộc (constraint propagation) được sử dụng trong CSP (Constraint Satisfaction Problems – bài toán thỏa mãn ràng buộc), ví dụ như Sudoku, lập thời khóa biểu, bản đồ tô màu...
- Mục tiêu của AC-3: Đảm bảo rằng tất cả các cung (arc) trong bài toán là consistency — tức là với mỗi giá trị có thể của một biến, tồn tại ít nhất một giá trị phù hợp ở biến liên quan.
- Thuật ngữ cần biết:
•	CSP: Bài toán gồm:
o	Tập biến X = {X1, X2, ..., Xn}
o	Tập miền giá trị D = {D1, D2, ..., Dn} tương ứng với các biến
o	Tập ràng buộc (constraints) giữa các biến
•	Arc (cung): Một cặp (Xi, Xj) nghĩa là ta đang kiểm tra ràng buộc từ biến Xi đến Xj.
•	Arc-consistent: Một cung (Xi, Xj) là arc-consistent nếu với mỗi giá trị x trong Di, tồn tại ít nhất một giá trị y trong Dj sao cho (x, y) thỏa mãn ràng buộc giữa Xi và Xj.
- Ý tưởng của AC-3:
•	Khởi tạo hàng đợi gồm tất cả các cung (Xi, Xj) có ràng buộc giữa các biến.
•	Lặp qua từng cung trong hàng đợi:
o	Nếu phát hiện một giá trị trong Di không còn giá trị phù hợp trong Dj, thì xóa giá trị đó khỏi Di.
o	Nếu có sự thay đổi, ta thêm lại tất cả cung (Xk, Xi) (với Xk ≠ Xj) vào hàng đợi để kiểm tra tiếp.
•	Kết thúc khi hàng đợi rỗng, nghĩa là không còn gì cần cập nhật.

 
-  Thuật toán AC-3 để lọc Domains giá trị của chương trình trong bài toán 8 ô chữ ở đây bao gồm các ràng buộc: Các ô có giá trị bằng nhau, các ô có giá trị tăng dần, các giá trị chẵn lẻ xen kẽ, có giá trị xen kẽ và phải khác nhau, các ô đối xứng thì cùng chẵn hoặc lẽ.

 
-  Ta có thể chỉnh giá trị cho Domain giá trị ban của của một biến.
 
-  Trên đây là demo việc lọc domains với điều kiện “Các ô chẵn lẽ xen kẽ và khác nhau”, ta thấy khi ta thiết lập giá trị ban đầu cho biến 5 có domain giá trị là 8 (số chẵn) thì khi lọc domain giá trị của các ô kề ô 5 (ô 2, 4, 8) sẽ bị loại bỏ giá trị chẵn, tương tự với các ô kề các ô này.
 
