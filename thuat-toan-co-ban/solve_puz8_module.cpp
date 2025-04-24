#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <unordered_set>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
using namespace std;



// ====================================================
struct Node {
    vector<vector<int>> value;
    Node* parent;
    vector<Node*> children;
    Node(vector<vector<int>> val, Node* p = nullptr) : value(val), parent(p) {}
};


// Trạng thái đích
vector<vector<int>> goal = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 0}
};

// Tọa độ di chuyển (trái, phải, lên, xuống)
int moveX[] = {0, 0, -1, 1};
int moveY[] = {-1, 1, 0, 0};

// Chuyển ma trận thành chuỗi để dễ lưu trong `unordered_set`
string boardToString(const vector<vector<int>>& board) {
    string s;
    for (const auto& row : board) {
        for (int num : row) {
            s += to_string(num);
        }
    }
    return s;
}

// Tìm vị trí số 0
pair<int, int> findIndex3x3(const vector<vector<int>>& matrix, int value) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matrix[i][j] == value) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

// Tạo danh sách trạng thái kế tiếp
vector<Node*> nextNodes(Node* node) {
    vector<Node*> nexts;
    auto board = node->value;
    auto [x0, y0] = findIndex3x3(board, 0);

    for (int i = 0; i < 4; i++) {
        int xc = x0 + moveX[i];
        int yc = y0 + moveY[i];

        if (xc >= 0 && xc < 3 && yc >= 0 && yc < 3) {
            vector<vector<int>> cp = board;
            swap(cp[x0][y0], cp[xc][yc]);
            nexts.push_back(new Node(cp, node));
        }
    }

    // Thêm children cho node hiện tại
    for (Node* child: nexts) {
        node->children.push_back(child);
    }

    return nexts;
}

// Hàm giải phóng tất cả node con
void deleteTree(Node* root) {
    if (!root) return;
    for (Node* child: root->children) {
        deleteTree(child);
    }
    delete root;
}




// ======================================================================================================
// BFS 
vector<vector<vector <int> > > bfs(Node* root, int& digged_nodes) {
    vector<vector<vector <int> > > solve_path;
    queue<Node*> q;
    unordered_set<string> visited;

    string startState = boardToString(root->value);
    visited.insert(startState);
    digged_nodes++;
    q.push(root);

    while (!q.empty()) {
        Node* node = q.front();
        q.pop();

        // Kiểm tra nếu tìm thấy trạng thái đích
        if (node->value == goal) {
            cout << "Da tim thay loi giai!\n";
            Node* temp = node;
            while (temp) {
                solve_path.push_back(temp->value);
                temp = temp->parent;
            }
            return solve_path;
        }

        // Duyệt trạng thái tiếp theo
        for (Node* next_node : nextNodes(node)) {
            string state = boardToString(next_node->value);
            if (visited.find(state) == visited.end()) { // Nếu chưa từng gặp trạng thái này
                visited.insert(state);
                digged_nodes++;
                q.push(next_node);
            }
        }
    }

    cout << "Khong tim thay loi giai!\n";
    return solve_path;
}

vector<vector<vector <int> > > solve_with_bfs(int i00, int i01, int i02, int i10, int i11, int i12, int i20, int i21, int i22) {
    vector<vector<int>> board = {
        {i00, i01, i02},
        {i10, i11, i12},
        {i20, i21, i22}
    };

    // Khối chứa thông tin: Số lượng node đã duyệt (0, 0), số bước giải (0, 1)
    vector<vector<int>> info = {
        {-1, -1, -1},
        {-1, -1, -1},
        {-1, -1, -1}
    };
    int digged_nodes = 0;
    int solved_path_length = 0;

    // Mảng chứa kết quả: Các node + khối thông tin ở cuối
    vector<vector<vector<int>>> result;

    Node* root = new Node(board);
    result = bfs(root, digged_nodes);
    solved_path_length = result.size();
    info[0][0] = digged_nodes;
    info[0][1] = solved_path_length;
    result.push_back(info);

    return result;
}



// ======================================================================================================
// DFS 
vector<vector<vector <int> > > dfs(Node* root, int& digged_nodes) {
    vector<vector<vector <int> > > solve_path;
    stack<Node*> s;
    unordered_set<string> visited;

    string startState = boardToString(root->value);
    visited.insert(startState);
    digged_nodes++;
    s.push(root);

    while (!s.empty()) {
        Node* node = s.top();
        s.pop();

        // Kiểm tra nếu tìm thấy trạng thái đích
        if (node->value == goal) {
            cout << "Da tim thay loi giai!\n";
            Node* temp = node;
            while (temp) {
                solve_path.push_back(temp->value);
                // for (const auto& row : temp->value) {
                //     for (int num : row) cout << num << " ";
                //     cout << endl;
                // }
                // cout << "------" << endl;
                temp = temp->parent;
            }
            return solve_path;
        }

        // Duyệt trạng thái tiếp theo
        for (Node* next_node : nextNodes(node)) {
            string state = boardToString(next_node->value);
            if (visited.find(state) == visited.end()) { // Nếu chưa từng gặp trạng thái này
                visited.insert(state);
                digged_nodes++;
                s.push(next_node);
            }
        }
    }

    cout << "Khong tim thay loi giai!\n";
    return solve_path;
}

vector<vector<vector <int> > > solve_with_dfs(int i00, int i01, int i02, int i10, int i11, int i12, int i20, int i21, int i22) {
    vector<vector<int>> board = {
        {i00, i01, i02},
        {i10, i11, i12},
        {i20, i21, i22}
    };

    // Khối chứa thông tin: Số lượng node đã duyệt (0, 0), số bước giải (0, 1)
    vector<vector<int>> info = {
        {-1, -1, -1},
        {-1, -1, -1},
        {-1, -1, -1}
    };
    int digged_nodes = 0;
    int solved_path_length = 0;

    // Mảng chứa kết quả: Các node + khối thông tin ở cuối
    vector<vector<vector<int>>> result;

    Node* root = new Node(board);
    result = dfs(root, digged_nodes);
    solved_path_length = result.size();
    info[0][0] = digged_nodes;
    info[0][1] = solved_path_length;
    result.push_back(info);

    return result;
}

// ======================================================================================================
// DLS
pair<Node*, bool> dls(Node* node, int depth, unordered_set<string>& visited) {
    string state = boardToString(node->value);
    if (visited.count(state)) return {nullptr, true}; // Tránh lặp vô hạn
    visited.insert(state);

    if (depth == 0) {
        return (node->value == goal) ? pair<Node*, bool>(node, true) : pair<Node*, bool>(nullptr, true);
    }

    bool any_remaining = false;
    for (Node* next_node : nextNodes(node)) {
        pair<Node*, bool> temp = dls(next_node, depth - 1, visited);
        Node* found = temp.first;
        bool remaining = temp.second;
        if (found) return {found, true};
        if (remaining) any_remaining = true;
    }
    return {nullptr, any_remaining};
}

// IDDFS
Node* iddfs(Node* root, int& visited_nodes_count) {
    int depth = 0;
    while (true) {
        unordered_set<string> visited;
        pair<Node*, bool> temp = dls(root, depth, visited);
        Node* found = temp.first;
        bool remaining = temp.second;

        if (found) return found;
        if (!remaining) return nullptr;

        depth++;
        visited_nodes_count += visited.size();
    }
}

vector<vector<vector<int>>> solve_with_iddfs(int i00, int i01, int i02, int i10, int i11, int i12, int i20, int i21, int i22) {
    vector<vector<int>> board = {
        {i00, i01, i02},
        {i10, i11, i12},
        {i20, i21, i22}
    };
    // Khối chứa thông tin: Số lượng node đã duyệt (0, 0), số bước giải (0, 1)
    vector<vector<int>> info = {
        {-1, -1, -1},
        {-1, -1, -1},
        {-1, -1, -1}
    };
    int visited_nodes = 0;
    int solved_path_length = 0;

    Node* root = new Node(board);
    Node* solution = iddfs(root, visited_nodes);


    if (solution) {
        vector<vector<vector<int>>> path;
        while (solution) {
            path.push_back(solution->value);
            solution = solution->parent;
        }
        solved_path_length = path.size();
        
        info[0][0] = visited_nodes;
        info[0][1] = solved_path_length;

        path.push_back(info);
        
        return path;
    } else {
        cout << "No solution found!\n";
        return vector<vector<vector<int>>>();
    }

    // Giải phóng bộ nhớ
    delete root;
}




namespace {
// // ======================================================================================================
// // Các hàm đánh giá trả về số âm càng nhỏ -> càng ít được ưu tiên

// // H0: Misplaced Tiles
// // Đánh giá theo số ô sai vị trí
// int H0(const Node* node) {
//     int misplaced = 0;
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             if (goal[i][j] != node->value[i][j]) {
//                 misplaced++;
//             }
//         }
//     }
//     return - misplaced;
// }

// // H1: Manhattan Distance
// int H1(const Node* node) {
//     int distance = 0;
//     int right_place[9][2] = {{2, 2}, {0, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1}, {1, 2}, {2, 0}, {2, 1}};
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             int val = node->value[i][j];
//             distance += abs(i - right_place[val][0]) + abs(j - right_place[val][1]);
//         }
//     }
//     return - distance;
// }


// // H2: Linear Conflict



// // A_star
// vector<vector<int>> A_star(Node* root) {
//     unordered_set<string> visited;
//     auto cmp = [](const Node* a, const Node* b) {
//         return *a < *b;
//     };
//     priority_queue<Node*, vector<Node*>, decltype(cmp)> pq(cmp);
//     vector<Node*> children = nextNodes(root);

//     // Khởi tạo hàng đợi ưu tiên
//     for (Node* child : children) {
//         pq.push(child);
//     }

//     while (!pq.empty()) {
//         Node* node = pq.top();
//         pq.pop();

//         // Kiểm tra nếu tìm thấy trạng thái đích
//         if (node->value == goal) {
//             cout << "Da tim thay loi giai!\n";
//             return node->value;
//         }

//         // Duyệt trạng thái tiếp theo
//         for (Node* next_node : nextNodes(node)) {
//             string state = boardToString(next_node->value);
//             if (visited.find(state) == visited.end()) { // Nếu chưa từng gặp trạng thái này
//                 visited.insert(state);
//                 pq.push(next_node);
//             }
//         }
//     }

//     cout << "Khong tim thay loi giai!\n";
//     return vector<vector<int>>(3, vector<int>(3, -1));
// }

// vector<vector<vector <int> > > solve_with_A_star(int i00, int i01, int i02, int i10, int i11, int i12, int i20, int i21, int i22) {
//     vector<vector<int>> board = {
//         {i00, i01, i02},
//         {i10, i11, i12},
//         {i20, i21, i22}
//     };

//     // Khối chứa thông tin: Số lượng node đã duyệt (0, 0), số bước giải (0, 1)
//     vector<vector<int>> info = {
//         {-1, -1, -1},
//         {-1, -1, -1},
//         {-1, -1, -1}
//     };
//     int digged_nodes = 0;
//     int solved_path_length = 0;

//     // Mảng chứa kết quả: Các node + khối thông tin ở cuối
//     vector<vector<vector<int>>> path;
//     vector<vector<int>> result;

//     Node* root = new Node(board);
//     result = A_star(root);

//     solved_path_length = result.size();
//     info[0][0] = digged_nodes;
//     info[0][1] = solved_path_length;
//     path.push_back(info);

//     return path;
}

// ======================================================================================================
// Định nghĩa module Python
PYBIND11_MODULE(solve_puz8_module, m) {
    m.def("solve_with_bfs", &solve_with_bfs, "Hàm giải puz8 với bfs");
    m.def("solve_with_dfs", &solve_with_dfs, "Hàm giải puz8 với dfs");
    m.def("solve_with_iddfs", &solve_with_iddfs, "Hàm giải puz8 với iddfs");
}

